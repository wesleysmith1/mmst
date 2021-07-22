from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

import config


class PaymentInfo(Page):
    def vars_for_template(self):
        performance = self.participant.vars.get('payoff', -1)
        performance_usd = c(performance / config.lira_per_dollar)

        payment = self.player.final_payment = performance_usd + config.participation_fee
        self.player.payment_round = self.participant.vars.get('payment_round', -1)

        return dict(
            final_payment_usd=payment.to_real_world_currency(self.session),
            final_payment_lira=int(performance / config.lira_per_dollar * 100),
            participation_usd=config.participation_fee,
            performance_lira=performance,
            performance_usd=performance_usd
        )

class Email(Page):
    form_model='player'
    form_fields=['email']


class Final(Page):
    pass


page_sequence = [PaymentInfo, Email, Final]
