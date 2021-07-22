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
from trivia.helpers import get_question
import numpy as np

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""

import requests


class Constants(BaseConstants):
    name_in_url = 'pilot_instructions'
    players_per_group = None
    num_rounds = 1

    worker_earnings = config.worker_earnings
    worker_bonus = config.worker_bonus

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

    def set_payoffs(self):
        pass


class Player(BasePlayer):
    pass