from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from helpers import formatted_pilot_key

import config_constants, config

from helpers import get_role, get_round_key, formatted_key
from trivia.helpers import get_question


class Payment(Page):

    def vars_for_template(self):

        participation_usd = c(config.participation_fee)

        performance_lira = int(self.participant.payoff * config.lira_per_dollar)
        performance_usd = self.participant.payoff

        # save final payment so it appears in data
        self.player.final_payment = participation_usd + self.participant.payoff

        return dict(
            performance_lira=performance_lira,
            participation_usd=participation_usd,
            performance_usd=performance_usd,
        )

class Email(Page):
    form_model='player'
    form_fields=['email']


class Final(Page):
    pass


page_sequence = [Payment, Email, Final]