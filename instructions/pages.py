from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

import config_constants
import config

from helpers import get_role, formatted_key

from trivia.helpers import get_token

def get_vars(self):
    return dict(
        bonus_setting = config.bonus_setting,
        discretion = config.discretion,
        # role=get_role(self.participant.id),

        manager_earnings=config.manager_earnings,
        manager_trivia_earnings=config.trivia_earnings,
        worker_earnings=config.worker_earnings,
        manager_bonus_contrib=int(config.manager_bonus_percentage * 100),
        standard_bonus=config.worker_bonus,
        standard_contrib=config.manager_contrib,

        pilot_percentage_one=config.pilot_percentage_one,
        pilot_grids_one=config.pilot_grids_one,
        pilot_percentage_two=config.pilot_percentage_two,
        pilot_grids_two=config.pilot_grids_two,
        pilot_participants=config.pilot_participants,
    )

class Introduction(Page):
    pass

class Instructions1(Page):
    pass

class Instructions1Quiz(Page):
    form_model='player'
    form_fields=['q1', 'q2']

    @staticmethod
    def error_message(values):

        incorrect = []
        for index, key in enumerate(values):
            if Constants.general_answers[key] != values[key]:
                incorrect.append(index+1)

        if len(incorrect) == 0:
            return

        return f"The following questions were answered incorectly {incorrect}"


class Instructions2(Page):

    def vars_for_template(self):
        vars = get_vars(self)
        fkey = formatted_key(0)
        vars['key'] = fkey

        return vars

    def before_next_page(self):
        pass
        # todo: this fails sometimes... fix pls
        # self.participant.vars['trivia_token'] = get_token()

class WInstructions2Quiz(Page):
    form_model='player'
    form_fields=[
        'wq3',
        'wq4',
        'wq5',
    ]

    @staticmethod
    def error_message(values):

        incorrect = []
        for index, key in enumerate(values):
            if Constants.worker_answers[key] != values[key]:
                incorrect.append(index+1)

        if len(incorrect) == 0:
            return

        return f"The following questions were answered incorectly {incorrect}"

    def is_displayed(self):
        return self.player.role == Constants.worker_role

class MInstructions2Quiz(Page):
    form_model='player'
    form_fields=[
        'mq3',
        'mq4',
        'mq5',
    ]

    @staticmethod
    def error_message(values):

        incorrect = []
        for index, key in enumerate(values):
            if Constants.manager_answers[key] != values[key]:
                incorrect.append(index+1)

        if len(incorrect) == 0:
            return

        return f"The following questions were answered incorectly {incorrect}"

    def is_displayed(self):
        return self.player.role == Constants.manager_role

# discretion - participation treatment pages
class DPInstructions(Page):
    def vars_for_template(self):
        return get_vars(self)

# discretion - no participation treatment pages
class DNPInstructions(Page):
    def vars_for_template(self):
        return get_vars(self)

# discretion - negotiation treatment pages
class DNInstructions(Page):
    def vars_for_template(self):
        return get_vars(self)

# no discretion - participation treatment pages
class NDPInstructions(Page):
    def vars_for_template(self):
        return get_vars(self)

# no discretion - no participation treatment pages
class NDNPInstructions(Page):
    def vars_for_template(self):
        return get_vars(self)

# no discretion - negotiation treatment pages
class NDNInstructions(Page):
    def vars_for_template(self):
        return get_vars(self)

class WInstructions3Quiz(Page):
    form_model='player'
    form_fields=[
        'wq6',
        'wq7',
        'wq8',
        'wq9',
        'wq10',
        'wq11',
        'wq12',
        'wq13',
        'wq14',
    ]

    # remove fields if they are not part of configured treatment
    if not config.discretion:
        form_fields.remove('wq12')

    if config.discretion:
        form_fields.remove('wq11')

    if config.bonus_setting != config_constants.NEGOTIATION:
        form_fields.remove('wq10')

    if config.bonus_setting != config_constants.PARTICIPATION:
        form_fields.remove('wq9')

    if config.bonus_setting != config_constants.NO_PARTICIPATION:
        form_fields.remove('wq8')

    @staticmethod
    def error_message(values):
        incorrect = []
        for index, key in enumerate(values):
            if Constants.worker_answers[key] != values[key]:
                incorrect.append(index+1)

        if len(incorrect) == 0:
            return

        return f"The following questions were answered incorectly {incorrect}"

    def is_displayed(self):
        return self.player.role == Constants.worker_role

class MInstructions3Quiz(Page):
    form_model='player'
    temp=[
        'mq6',
        'mq7',
        'mq8',
        'mq9',
        'mq10',
        'mq11',
        'mq12'
    ]

    if not config.discretion:
        temp.remove('mq11')

    if config.bonus_setting != config_constants.NEGOTIATION:
        temp.remove('mq9')
        temp.remove('mq7')

    if config.bonus_setting != config_constants.PARTICIPATION:
        temp.remove('mq8')

    form_fields = temp

    @staticmethod
    def error_message(values):
        incorrect = []
        for index, key in enumerate(values):
            if Constants.manager_answers[key] != values[key]:
                incorrect.append(index+1)

        if len(incorrect) == 0:
            return

        return f"The following questions were answered incorectly {incorrect}"

    def is_displayed(self):
        return self.player.role == Constants.manager_role

# define page_sequence based off treatment configuration
x = [
        Introduction, 
        Instructions1, 
        Instructions1Quiz, 
        Instructions2, 
        WInstructions2Quiz,
        MInstructions2Quiz,
    ]

if config.discretion:
    if config.bonus_setting == config_constants.NO_PARTICIPATION:

        # page_sequence = [Instructions, DNPInstructions, Practice]
        x.append(DNPInstructions)

    elif config.bonus_setting == config_constants.PARTICIPATION:
        # page_sequence = [Instructions, DPInstructions, Practice]
        x.append(DPInstructions)

    elif config.bonus_setting == config_constants.NEGOTIATION:

        # page_sequence = [Instructions, DNInstructions, Practice]
        x.append(DNInstructions)

elif not config.discretion:
    if config.bonus_setting == config_constants.NO_PARTICIPATION:
        
        # page_sequence = [Instructions, NDNPInstructions, Practice]
        x.append(NDNPInstructions)

    elif config.bonus_setting == config_constants.PARTICIPATION:
        
        # page_sequence = [Instructions, NDPInstructions, Practice]
        x.append(NDPInstructions)

    elif config.bonus_setting == config_constants.NEGOTIATION:
        
        # page_sequence = [Instructions, NDNInstructions, Practice]
        x.append(NDNInstructions)

x.append(WInstructions3Quiz)
x.append(MInstructions3Quiz)
page_sequence = x