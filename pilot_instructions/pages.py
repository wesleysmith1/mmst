from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from helpers import formatted_pilot_key

import config_constants, config

from helpers import get_role, get_round_key, formatted_key
from trivia.helpers import get_question


class PilotInstructions(Page):

    def vars_for_template(self):
        key = formatted_pilot_key(0)

        return dict(key=key)
        

page_sequence = [PilotInstructions,]
