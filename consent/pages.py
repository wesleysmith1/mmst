from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Consent(Page):
    pass


page_sequence = [Consent]
