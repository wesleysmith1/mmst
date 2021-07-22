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
    num_rounds = 1
    name_in_url = 'pilot_payment'
    players_per_group = None

    manager_role = 'manager'
    worker_role = 'worker'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    final_payment = models.CurrencyField()
    email = models.StringField()