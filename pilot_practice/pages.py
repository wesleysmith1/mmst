from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

import config_constants, config

from helpers import get_role, formatted_pilot_key
from trivia.helpers import get_question


class Game(Page):
    timeout_seconds = 30

    live_method = 'live_game'

    def vars_for_template(self):

        vars = dict()      

        key = formatted_pilot_key(self.round_number)

        vars.update({
            'key': key,
        })

        return vars

class Results(Page):
    timeout_seconds = 15

page_sequence = [Game, Results]
