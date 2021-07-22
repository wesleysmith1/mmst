from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

import config_constants
import config

from helpers import get_role, formatted_key

from trivia.helpers import get_token

class PracticeWait(WaitPage):
    pass


class Practice(Page):
    timeout_seconds = 60
    live_method = 'live_game'
    
    def vars_for_template(self):
        vars = {
            'key': formatted_key(0),
        }
        return vars

class Results(Page):
    timeout_seconds = 60

    def is_displayed(self):
        return self.player.role == Constants.worker_role
    

page_sequence = [PracticeWait,Practice, Results]