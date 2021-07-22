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
from helpers import get_pilot_key
from trivia.helpers import get_question
import numpy as np

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""

import requests


class Constants(BaseConstants):
    name_in_url = 'pilot'
    players_per_group = None
    num_rounds = 5

    worker_earnings = config.pilot_worker_earnings
    worker_bonus = config.worker_bonus

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    decodes_completed = models.IntegerField(initial=0)
    decodes_incorrect = models.IntegerField(initial=0)
    decodes_earnings = models.IntegerField(initial=0)

    def calculate_payoff(self):

        self.participant.vars['pilot_earnings'] = self.participant.vars.get('pilot_earnings', 0) + (self.decodes_completed * Constants.worker_earnings / config.lira_per_dollar)
        self.payoff = self.decodes_completed * Constants.worker_earnings / config.lira_per_dollar

    def live_game(self, data):
        
        decode = data # get data mon

        let_responses = data['responses']
        num_codes = data['codes']
        key = get_pilot_key(self.round_number)
        
        if len(num_codes) != 1:
            raise ValueError('Number of items decoded does not match requirements for this round.')
        
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

