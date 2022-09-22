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
from trivia.helpers import get_question, get_token
from helpers import get_round_key

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'practice'
    players_per_group = None
    num_rounds = 1

    # manager = 'manager'
    # worker = 'worker'

    manager_role = 'manager'
    worker_role = 'worker'

class Subsession(BaseSubsession):
    
    def creating_session(self):
        players = self.get_players()

        # set role
        for player in players:

            if player.role == Constants.manager_role:
                player.participant.vars['trivia_token'] = get_token()

        groups = self.get_groups()
        for group in groups:
            group.discretion = self.session.config['vars']['discretion']
            group.bonus_setting = self.session.config['vars']['bonus_setting']


class Group(BaseGroup):
    discretion = models.BooleanField()
    bonus_setting = models.StringField()


class Player(BasePlayer):
    trivia_count = models.IntegerField(initial=0)
    decodes_completed = models.IntegerField(initial=0)
    decodes_incorrect = models.IntegerField(initial=0)
    trivia_earnings = models.IntegerField(initial=0)
    last_trivia_answer = models.StringField()
    decodes_earnings = models.IntegerField(initial=0)
    # custom_role = models.StringField()

    def get_trivia_question(self):
        question = get_question(self.participant.vars.get('trivia_token', None))
        self.participant.vars['question'] = question.copy() # copy to prevent deletion
        del question['solution']
        return question

    def check_trivia_answer(self, answer):
        if self.role == Constants.manager_role:
            if self.participant.vars['question']['solution'] == answer:
                self.trivia_count += 1
        else:
            raise ValueError('Cannot check trivia answer for worker')
    
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
            key = get_round_key(0)
            
            
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