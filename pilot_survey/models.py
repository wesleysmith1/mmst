from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'pilot_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(label='What is your age?', min=18, max=125)

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Prefer not to answer', 'Prefer not to answer']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    native_english = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Is your native language English?',
        widget=widgets.RadioSelect()
    )
