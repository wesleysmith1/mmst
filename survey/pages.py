from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

import config, config_constants


class WorkerSurvey1(Page):
    form_model = 'player'
    form_fields = [
            's1',
            's2',
            's3',
            's4',
            's5',
            's6',
            's7',
            's8',
            's9',
            'wro1', 
            'wro2', 
            'wro3', 
            'wro4',
        ]
    if not config.discretion:
        form_fields.remove('wro4')
        form_fields.remove('wro1')

    def is_displayed(self):
        return self.player.role == 'worker'

    def vars_for_template(self):
        return dict(
            # custom_role=self.participant.vars.get('custom_role', 'manager'),
            discretion=config.discretion,
            bonus_setting=config.bonus_setting,
        )

    @staticmethod
    def error_message(values):
        '''Ensure that the rank order responses are distinct'''
        inputs = []
        r = 5 if config.discretion else 3 # ro4 question is only for discretion
        for i in range(1,r):
            val = values.get(f"ro{i}")
            if not val:
                continue
            if val in inputs:
                return "Responses to news preferences rank order question must not be duplicated"
            else:
                inputs.append(val)

class ManagerSurvey1(Page):
    form_model = 'player'
    form_fields = [
            's1',
            's2',
            's3',
            's9',
            'mro1', 
            'mro2', 
            'mro3', 
            'mro4',
        ]
    if not config.discretion:
        form_fields.remove('mro4')

    def is_displayed(self):
        return self.player.role == Constants.manager_role

    def vars_for_template(self):
        return dict(
            # custom_role=self.participant.vars.get('custom_role', 'manager'),
            discretion=config.discretion,
            bonus_setting=config.bonus_setting,
        )

    @staticmethod
    def error_message(values):
        '''Ensure that the rank order responses are distinct'''
        inputs = []
        r = 5 if config.discretion else 4 # mro4 question is only for discretion
        for i in range(1,r):
            val = values[f"mro{i}"]
            if val in inputs:
                return "Responses to news preferences rank order question must not be duplicated"
            else:
                inputs.append(val)

class Survey2(Page):
    form_model = 'player'
    form_fields = [
        'ttm1',
        'ttm2',
    ]
    if config.bonus_setting == config_constants.NO_PARTICIPATION:
        form_fields.remove('ttm1')

    def is_displayed(self):
        return self.player.role == Constants.worker_role

class Survey3(Page):
    form_model = 'player'
    form_fields = [
        'pj1',
        'pj2',
        'pj3',
    ]

class ManagerSurvey2(Page):
    form_model = 'player'
    if config.discretion:
        form_fields = [
            'd1',
            'd2',
            'd3',
            'd4',
            'd5',
        ]
    else:
        form_fields = [
            'nd1',
            'nd2',
            'nd3',
            'nd4',
        ]
    
    def is_displayed(self):
        return self.player.role == Constants.manager_role

class ManagerSurvey3(Page):
    form_model = 'player'
    if config.discretion:
        form_fields = [
            'd5',
        ]
    else:
        form_fields = [
            'd5',
        ]
    
    def is_displayed(self):
        return self.player.role == Constants.manager_role and config.discretion


class Demographics(Page):
    form_model='player'
    form_fields=[
        'gender',
        'age',
        'native_english',
    ]


page_sequence = [ManagerSurvey1, WorkerSurvey1, Survey2, Survey3, ManagerSurvey2, ManagerSurvey3, Demographics]
