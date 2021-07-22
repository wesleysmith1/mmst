from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

import config


class Survey(Page):
    form_model = 'player'
    form_fields = [
            'age',
            'gender',
            'native_english',
        ]


page_sequence = [Survey,]
