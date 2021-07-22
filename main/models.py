from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from config import bonus_setting, discretion
import config_constants
import config
from helpers import get_round_key
from trivia.helpers import get_question, get_token
import numpy as np

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""

import requests


class Constants(BaseConstants):
    name_in_url = 'bonus'
    players_per_group = 2
    num_rounds = config.production_rounds

    # manager = 'manager'
    # worker = 'worker'

    manager_role = 'manager'
    worker_role = 'worker'

    # Final round of bonus negotiation stage
    final_round = 10

    manager_earnings = config.manager_earnings
    worker_earnings = config.worker_earnings
    trivia_earnings = config.trivia_earnings
    manager_contrib = config.manager_contrib
    worker_bonus = config.worker_bonus
    manager_contrib_percentage = config.manager_bonus_percentage


class Subsession(BaseSubsession):
    
    def creating_session(self):

        self.group_randomly(fixed_id_in_group=True)

        players = self.get_players()

        if len(players) % 2:
            raise ValueError('Odd numer of participants. There needs to be equal number of managers and workers for creating groups')

        # set role and calculate if round is difficult or not
        for player in players:

            if player.role == Constants.manager_role:
                player.participant.vars['trivia_token'] = get_token()
            elif player.role == Constants.worker_role:
                player.group.difficult = player.difficult = bool(np.random.binomial(1, config.probability_difficult)) 
            else:
                raise ValueError('This player does not have a set role!')

            # if player.participant.id % 2:
            #     # todo: fix this
            #     player.role = Constants.manager_role
            #     # retrieve and set trivia token
            #     player.participant.vars['trivia_token'] = get_token()
            #     pass
            # else:
            #     player.custom_role = 'worker'
            #     player.group.difficult = player.difficult = bool(np.random.binomial(1, config.probability_difficult)) 
                
            # player.participant.vars['custom_role'] = player.custom_role
            player.participant.vars['payment_round'] = np.random.randint(Constants.num_rounds) + 1

class Group(BaseGroup):
    target_round = models.IntegerField(initial=1)
    proposed_target = models.IntegerField(initial=0)
    final_target = models.IntegerField(min=0, initial=-1)
    difficult = models.BooleanField()
    bonus = models.IntegerField(min=0, initial=Constants.worker_bonus) #todo: on discretion the worker can get a fraction of a point. do we want this?
    '''
    negotiation stages:
        1 worker sets bonus 
        2 manager accepts or sets bonus
        3 worker accepts or sets bonus
        4 manager accepts or sets bonus
        5 worker accepts or sets bonus
        6 manager accepts or sets bonus
        7 worker accepts or sets bonus
        8 manager accepts or sets final bonus
        
        **if bonus is accepted advance to round 9
    '''

    def get_worker(self):
        players = self.get_players()
        for player in players:
            if player.role == Constants.worker_role:
                return player
        else:
            pass


    def target_reached(self, player):
        '''return bool if target was reached by worker'''
        if player.role == Constants.manager_role:
            worker = player.other_player()
        else:
            worker = player

        if worker.decodes_completed >= self.final_target:
            return True
        else:
            return False


class Player(BasePlayer):
    difficult = models.BooleanField()
    trivia_count = models.IntegerField(initial=0)
    decodes_completed = models.IntegerField(initial=0)
    decodes_incorrect = models.IntegerField(initial=0)
    trivia_earnings = models.IntegerField(initial=0)
    last_trivia_answer = models.StringField()
    decodes_earnings = models.IntegerField(initial=0)
    # custom_role = models.StringField()
    payoff_lira = models.FloatField(initial=0)

    def get_trivia_question(self):
        token = self.participant.vars.get('trivia_token', None)
        question = get_question(token)
        self.participant.vars['question'] = question.copy() # copy to prevent deletion
        del question['solution']
        return question

    def check_trivia_answer(self, answer):
        if self.role == Constants.manager_role:
            if self.participant.vars['question']['solution'] == answer:
                self.trivia_count += 1
        else:
            raise ValueError('Cannot check trivia answer for worker')


    def calculate_payoff(self):
        # todo: calculate payment
        if self.role == Constants.manager_role:
        
            self.trivia_earnings = self.trivia_count * Constants.trivia_earnings
            self.payoff_lira += self.trivia_earnings
            
            worker = self.other_player()
            self.decodes_earnings = worker.decodes_completed * Constants.manager_earnings
            self.payoff_lira += self.decodes_earnings
            
        else:
            self.decodes_earnings = self.decodes_completed * Constants.worker_earnings
            self.payoff_lira = self.decodes_earnings
        
        self.apply_bonus()

        
        if self.participant.vars['payment_round'] == self.round_number:
            self.participant.vars['payoff'] = self.payoff_lira

    def apply_bonus(self):
        if self.group.target_reached(self):
            """Manager pays part of bonus if target reached"""

            if self.role == Constants.manager_role:
                self.payoff_lira -= self.group.bonus * Constants.manager_contrib_percentage
            elif self.role == Constants.worker_role:
                self.payoff_lira += self.group.bonus
        else:
            self.group.bonus = 0

    def is_manager(self):
        return self.role == Constants.manager_role

    def is_worker(self):
        return self.role == Constants.worker_role

    def other_player(self):
        return self.get_others_in_group()[0]

    def live_target(self, data):
        """data format {accepted: bool, proposal: num}"""

        # other player id in group
        other_id = self.get_others_in_group()[0].id_in_group

        if data.get('accept'):

            # self.group.target_round = Constants.final_round
            self.group.final_target = self.group.proposed_target

            update = dict(accepted=True, round=self.group.target_round,)

            return {self.id_in_group: update, other_id: update, }
        
        elif data.get('worker_decline'):
            # the worker declined proposed target in final round
            self.group.target_round += 1
            update = dict(round=self.group.target_round)
            return {other_id: update}

        else:
            # todo: state michine thingy to make sure process is not broken
            self.group.target_round += 1
            self.group.proposed_target = int(data['proposal'])

            if self.group.target_round >= Constants.final_round:
                self.group.final_target = self.group.proposed_target

            # updated group data
            update = dict(round=self.group.target_round, proposal=self.group.proposed_target)

            return {self.id_in_group: update, other_id: update}

    def live_game(self, data):

        if self.role == Constants.manager_role:

            user_response = data['answer']

            self.check_trivia_answer(user_response)

            question = self.get_trivia_question()

            return {self.id_in_group: {'question': question}}

        elif self.role == Constants.worker_role:


            decode = data # get data mon

            let_responses = data['responses']
            num_codes = data['codes']
            key = get_round_key(self.round_number)

            
            if (self.difficult and len(num_codes) != 2) or (not self.difficult and len(num_codes) != 1):
                raise ValueError('Number of items decoded does not match the difficulty for this round.')
            
            for x in zip(num_codes, let_responses):
                code = x[0] # number
                response = x[1].upper() # letter
                if code == key.get(response):
                    continue
                else:
                    self.decodes_incorrect += 1
                    break
            else: 
                self.decodes_completed += 1
