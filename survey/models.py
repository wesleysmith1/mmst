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
import config


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = 2
    num_rounds = 1

    manager_role = 'manager'
    worker_role = 'worker'


class Subsession(BaseSubsession):

    # this code is run in case it is demo mode
    def creating_session(self):
        pass
                

class Group(BaseGroup):
    pass

scale_options = [1,2,3,4,5,6,7]
worker_rank_order = [1,2,3,4]
manager_rank_order = [1,2,3,4]

if not config.discretion:
    manager_rank_order.remove(4)

    # there was a change. no rank order questions for discretion condition
    # worker_rank_order.remove(4)
    # Worker does not answer ro1
    # worker_rank_order.remove(3)

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

    # scale questions
    s1 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="The way that payoffs were determined for me was fair."
    )
    # todo: make role dynamic
    s2 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="The way that payoffs were determined for the manager/worker was fair."
    )
    s3 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="The way that the target was set was fair."
    )

    # worker only
    s4 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I feel I was good at the decoding task."
    )
    s5 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I found this decoding task to be difficult.",
    )
    s6 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="My performance was a resonable representation of my skill."
    )
    s7 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I felt it was important to do well on the production task."
    )
    s8 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I found the decoding task to be enjoyable.",
    )
    # ================================================================================================
    
    s9 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I consider myself to be an overachiever."
    )

    #==============================================================

    # worker only
    # rank order

    # discretion only
    if config.discretion:
        wro1 = models.IntegerField(
            choices=worker_rank_order,
            label="Fairness"
        )
        wro2 = models.IntegerField(
            choices=worker_rank_order,
            label="Motivation",
        )
        wro3 = models.IntegerField(
            choices=worker_rank_order,
            label="pay"
        )
        wro4 = models.IntegerField(
            choices=worker_rank_order,
            label="Discretion"
        )
    #==============================================================

    # target to motivation
    ttm1 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Having input into the target-setting process motivated me to achieve the target."
    )
    ttm2 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I was committed to meeting the target."
    )

    # prodedural justice
    pj1 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="It is more important that rules and prodedures are equally fair to everyone than that everyone is paid a fair amount.",
    )
    pj2 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="It is more important for people to be paid a fair amount than for the procedures used to determine compensation to be fair."
    )
    pj3 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Performance evaluations should consider the individual and the situation rather than be based on rules and procedures",
    )

    # manager only questions ============================================================

    # rank order
    mro1 = models.IntegerField(
        choices=manager_rank_order,
        label="Fairness"
    )
    mro2 = models.IntegerField(
        choices=manager_rank_order,
        label="Motivation",
    )
    mro3 = models.IntegerField(
        choices=manager_rank_order,
        label="pay"
    )
    # discretion only
    if config.discretion:
        mro4 = models.IntegerField(
            choices=manager_rank_order,
            label="Discretion"
        )
    #==============================================================

    # discretion
    d1 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could adjust the worker’s bonus amount at the end of the period made me think more carefully about the worker’s target.",
    )
    d2 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could adjust the worker’s bonus amount at the end of the period made me put more effort into setting the worker’s target.",
    )
    d3 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could adjust the worker’s bonus amount at the end of the period made me feel more responsible for the worker’s bonus outcome.",
    )
    d4 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could adjust the worker’s bonus amount at the end of the period made me feel more responsible for setting an appropriate target for the worker.",
    )
    d5 = models.IntegerField(
        label="I adjusted (did not adjust) the worker’s bonus because:",
        choices=[
            "I wanted to motivate future performance.",
            "I wanted to show that I appreciated the worker setting a difficult target.",
            "I wanted the worker's compensation to be fail.",
            "I wanted the worker to trust me.",
            "I wanted the worker's compensation to reflect their effort.",
        ]
    )

    # no discretion
    nd1 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could not adjust the worker's bonus amount at the end of the period made me think more carefully about the worker's target.",
    )
    nd2 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Know that I could not adjust the worker's bonus amount at the end of the period made me put more effort into setting the worker's target.",
    )
    nd3 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could not adjust the worker's bonus amount at the end of the period made me feel more responsible for the worker's bonus outcome.",
    )
    nd4 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could not adjust the worker's bonus amount at the end of the period made me feel more responsible for setting an appropiate target for the worker.",
    )

    # ========================================================================================================================