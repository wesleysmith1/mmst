from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants, Player

import config, config_constants


class WSurvey1(Page):
    form_model = 'player'

    form_fields = [
        'q1',
        'q2',
        'q3',
        'q4',
        'q5',
        'q6',
        'q7',
        'q8',
        'q9',
    ]

    def is_displayed(self):
        return self.player.role == 'worker'

    def vars_for_template(self):
        return dict(
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )

class MSurvey1(Page):
    form_model = 'player'

    form_fields = [
            'q1',
            'q2',
            'q3',
            'q9',
        ]

    def is_displayed(self):
        return self.player.role == 'manager'

    def vars_for_template(self):
        return dict(
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )


class WSurvey2(Page):
    form_model = 'player'

    def get_form_fields(self):

        form_fields = [
        ]

        if self.group.discretion:
            if self.group.bonus_setting == config_constants.PARTICIPATION:
                form_fields.append('wq10a')
                form_fields.append('wq10b')
                form_fields.append('wq10c')
                form_fields.append('wq10d')
            elif self.group.bonus_setting == config_constants.NEGOTIATION:
                form_fields.append('wq10a')
                form_fields.append('wq10b')
                form_fields.append('wq10c')
                form_fields.append('wq10d')
            elif self.group.bonus_setting == config_constants.NO_PARTICIPATION:
                pass
        elif not self.group.discretion:
            if self.group.bonus_setting == config_constants.PARTICIPATION:
                form_fields.append('wq10a')
                form_fields.append('wq10b')
                form_fields.append('wq10c')
            elif self.group.bonus_setting == config_constants.NEGOTIATION:
                form_fields.append('wq10a')
                form_fields.append('wq10b')
                form_fields.append('wq10c')
            elif self.group.bonus_setting == config_constants.NO_PARTICIPATION:
                pass

        return form_fields

        
    @staticmethod
    def error_message(values):

        if len(set(values.values())) != len(values.values()):
            return "Each response must have a different number."

    def is_displayed(self):
        return self.player.role == 'worker' and self.group.bonus_setting != config_constants.NO_PARTICIPATION

    def vars_for_template(self):

        if not self.group.discretion or self.group.bonus_setting == config_constants.NO_PARTICIPATION:
            important = 3
        else:
            important = 4

        return dict(
            important=important,
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )


class MSurvey2(Page):
    form_model = 'player'

    def get_form_fields(self):

        form_fields = []

        if self.group.discretion:
            if self.group.bonus_setting == config_constants.PARTICIPATION:
                pass
            elif self.group.bonus_setting == config_constants.NEGOTIATION:
                form_fields.append('mq10a')
                form_fields.append('mq10b')
                form_fields.append('mq10c')
                # form_fields.append('mq10d')
            elif self.group.bonus_setting == config_constants.NO_PARTICIPATION:
                form_fields.append('mq10a')
                form_fields.append('mq10b')
                form_fields.append('mq10c')
                # form_fields.append('mq10d')
        elif not self.group.discretion:
            if self.group.bonus_setting == config_constants.PARTICIPATION:
                pass
            elif self.group.bonus_setting == config_constants.NEGOTIATION:
                form_fields.append('mq10a')
                form_fields.append('mq10b')
                form_fields.append('mq10c')
            elif self.group.bonus_setting == config_constants.NO_PARTICIPATION:
                form_fields.append('mq10a')
                form_fields.append('mq10b')
                form_fields.append('mq10c')

        return form_fields

    def is_displayed(self):
        return self.player.role == 'manager' and self.group.bonus_setting != config_constants.PARTICIPATION

    @staticmethod
    def error_message(values):

        if len(set(values.values())) != len(values.values()):
            return "Each response must have a different number."
        

    def vars_for_template(self):

        if not self.group.discretion or self.group.bonus_setting == config_constants.PARTICIPATION:
            important = 3
        else:
            important = 4

        return dict(
            important=important,
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )


class WSurvey3(Page):
    """Target to motivation"""
    form_model = 'player'

    def get_form_fields(self):

        form_fields = [
            'q11',
        ]

        if self.group.bonus_setting in (config_constants.PARTICIPATION , config_constants.NEGOTIATION):
            form_fields = [
                'q11',
                'q12'
            ]
        else:
            form_fields = [
                'q11',
            ]

        return form_fields

    def is_displayed(self):
        return self.player.role == 'worker'

    def vars_for_template(self):
        return dict(
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )

class WSurvey4(Page):
    """Procedural justice questions"""
    form_model = 'player'
    form_fields = [
        'q13',
        'q14',
        'q15',
    ]

    def is_displayed(self):
        return self.player.role == 'worker'

    def vars_for_template(self):
        return dict(
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )

class MSurvey3(Page):
    """Procedural justice questions"""
    form_model = 'player'
    form_fields = [
        'q13',
        'q14',
        'q15',
    ]

    def is_displayed(self):
        return self.player.role == 'manager'

    def vars_for_template(self):
        return dict(
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )


class MSurvey3D(Page):
    """Manager only questions (discretion only)"""
    form_model = 'player'

    def get_form_fields(self):

        if self.group.bonus_setting == config_constants.NO_PARTICIPATION:
            return [
                'q16',
                'q17',
                'q18',
                'q19',
                # 'q20',
            ]
        elif self.group.bonus_setting == config_constants.NEGOTIATION:
            return [
                'q16',
                'q17',
                'q18',
                'q19',
                # 'q20',
            ]
        else:
            return [
                # 'q16',
                # 'q17',
                'q18',
                # 'q19',
                # 'q20',
            ]

    def is_displayed(self):
        return self.player.role == 'manager' and self.group.discretion

    def vars_for_template(self):
        return dict(
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )

class MSurvey4D(Page):
    """Manager only questions (discretion only)"""
    form_model = 'player'

    def get_form_fields(self):

        if self.group.bonus_setting == config_constants.PARTICIPATION:
            return [
                'q20',
                'q21',
                'q22',
                'q23',
                'q24',
            ]
        elif self.group.bonus_setting == config_constants.NEGOTIATION:
            return [
                'q20',
                'q21',
                'q22',
                'q23',
                'q24',
            ]
        else:
            return [
                'q20',
                'q22',
                'q23',
                'q24',
            ]

    def is_displayed(self):
        return self.player.role == 'manager' and self.group.discretion

    def vars_for_template(self):
        return dict(
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )

    @staticmethod
    def error_message(values):
        fields =  [
                'q20',
                'q21',
                'q22',
                'q23',
                'q24',
            ]

        total = 0
        for f in fields:
            total += values.get(f, 0)

        if total != 100:
            return f"The total of questions must equal 100. The current total is {total}."


class MSurvey3ND(Page):
    """Manager only questions (no discretion)"""
    form_model = 'player'

    def get_form_fields(self):

        if self.group.bonus_setting == config_constants.NO_PARTICIPATION:
            return [
                'q25',
                'q26',
                'q27',
                'q28',
            ]
        elif self.group.bonus_setting == config_constants.NEGOTIATION:
            return [
                'q25',
                'q26',
                'q27',
                'q28',
            ]
        else:
            return [
                # 'q25',
                # 'q26',
                'q27',
                # 'q28',
            ]

    def is_displayed(self):
        return self.player.role == 'manager' and not self.group.discretion

    def vars_for_template(self):
        return dict(
            discretion=self.group.discretion,
            bonus_setting=self.group.bonus_setting,
        )


class Demographics(Page):
    form_model='player'
    form_fields=[
        'gender',
        'age',
        'native_english',
    ]

# ======================================================================================

page_sequence = [WSurvey1, MSurvey1, WSurvey2, MSurvey2, WSurvey3, WSurvey4, MSurvey3, MSurvey3ND, MSurvey3D, MSurvey4D, Demographics]
