from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

import config_constants, config

from helpers import get_role, get_round_key, formatted_pilot_key
from trivia.helpers import get_question

class Introduction(Page):
    pass

class Game(Page):
    timeout_seconds = 120

    live_method = 'live_game'

    def vars_for_template(self):

        vars = dict()      

        key = formatted_pilot_key(self.round_number)

        vars.update({
            'key': key,
        })

        return vars

    def before_next_page(self):
        self.player.calculate_payoff()

class Results(Page):

    def vars_for_template(self):
        return dict(
            payoff=self.player.decodes_completed * Constants.worker_earnings
        )

page_sequence = [Game, Results]
