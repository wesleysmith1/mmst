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
import config, config_constants


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = 2
    num_rounds = 1

    manager_role = 'manager'
    worker_role = 'worker'


class Subsession(BaseSubsession):

    # this code is run in case it is demo mode
    def creating_session(self):                

        groups = self.get_groups()
        for group in groups:
            group.discretion = self.session.config['vars']['discretion']
            group.bonus_setting = self.session.config['vars']['bonus_setting']


class Group(BaseGroup):
    discretion = models.BooleanField()
    bonus_setting = models.StringField()


scale_options = [1,2,3,4,5,6,7]
# worker_rank_order = [1,2,3,4]
# manager_rank_order = [1,2,3,4]

# if not config.discretion:
#     manager_rank_order.remove(4)
#     worker_rank_order.remove(4)
# elif config.bonus_setting == config_constants.PARTICIPATION:
#     manager_rank_order.remove(4)
# elif config.bonus_setting == config_constants.NO_PARTICIPATION:
#     worker_rank_order.remove(4)

    # there was a change. no rank order questions for discretion condition
    # worker_rank_order.remove(4)
    # Worker does not answer ro1
    # worker_rank_order.remove(3)


class Player(BasePlayer):

    # scale questions
    q1 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="The way that payoffs were determined for me was fair."
    )
    q2 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="The way that payoffs were determined for the manager/worker was fair."
    )
    q3 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="The way that the target was set was fair."
    )
    # worker only
    q4 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I feel I was good at the decoding task."
    )
    # worker only
    q5 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I found this decoding task to be difficult.",
    )
    # worker only
    q6 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="My performance was a resonable representation of my skill."
    )
    # worker only
    q7 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I felt it was important to do well on the decoding task."
    )
    # worker only
    q8 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I found the decoding task to be enjoyable.",
    )
    q9 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I consider myself to be an overachiever."
    )
    #==============================================================

    # worker only: Please rank the following factors based on their importance in how you set the target, from the most important to the least important.
    # rank order

    # discretion only
    wq10a = models.IntegerField(
        label="Fairness",
        choices=[1,2,3]
    )
    wq10b = models.IntegerField(
        label="Motivation",
        choices=[1,2,3]
    )
    wq10c = models.IntegerField(
        label="pay",
        choices=[1,2,3]
    )
    #==============================================================

    # worker only: Please rank the following factors based on their importance in how you set the target, from the most important to the least important.
    # rank order

    #==============================================================
    # discretion only
    mq10a = models.IntegerField(
        label="Fairness",
        choices=[1,2,3]
    )
    mq10b = models.IntegerField(
        label="Motivation",
        choices=[1,2,3]
    )
    mq10c = models.IntegerField(
        label="pay",
        choices=[1,2,3]
    )
    #==============================================================

    # (managers only – no participation condition)
    mq11a = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I considered my discretion to adjust the worker’s bonus at the end of each period when setting the target at the beginning of the period."
    )

    # (managers only – negotiation condition)
    mq11b = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I considered my discretion to adjust the worker’s bonus at the end of each period during the target negotiation."
    )

    # (workers only – participation condition) 
    wq11a = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I considered the manager’s discretion to adjust my bonus at the end of each period when setting the target at the beginning of the period."
    )

    # (workers only – negotiation condition)
    wq11b = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I considered the manager’s discretion to adjust my bonus at the end of each period during the target negotiation."
    )

    #==============================================================

    # target to motivation 
    # # workers only
    q12 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="I was committed to meeting the target."
    )
    # worker only
    q13 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Having input into the target-setting process motivated me to achieve the target."
    )

    # prodedural justice
    q14 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="It is more important that rules and prodedures are equally fair to everyone than that everyone is paid a fair amount.",
    )
    q15 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="It is more important for people to be paid a fair amount than for the procedures used to determine compensation to be fair."
    )
    q16 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Performance evaluations should consider the individual and the situation rather than be based on rules and procedures",
    )

    # manager discretion (no participation and negotiation conditions only)
    q17 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could adjust the worker's bonus amount at the end of the period made me think more carefully about the worker's target.",
    )
    # manager discretion (no participation and negotiation conditions only)
    q18 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could adjust the worker's bonus amount at the end of the period made me put more effort into setting the worker's target.",
    )
    # manager discretion ALL CONDITIONS
    q19 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could adjust the worker's bonus amount at the end of the period made me feel more responsible for the worker's bonus outcome.",
    )
    # manager discretion (no participation and negotiation conditions only)
    q20 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could adjust the worker's bonus amount at the end of the period made me feel more responsible for setting an appropriate target for the worker.",
    )

    # ===============all questions add to 100======================
    q21 = models.IntegerField(
        label="I wanted to motivate future performance.",
        max=100,
        min=0,
    )
    # participation and negotiation conditions only
    q22 = models.IntegerField(
        label="I wanted to show that I appreciated the worker setting a difficult target.",
        max=100,
        min=0,
    )
    q23 = models.IntegerField(
        label="I wanted the worker’s compensation to be fair.",
        max=100,
        min=0,
    )
    q24 = models.IntegerField(
        label="I wanted the worker to trust me.",
        max=100,
        min=0,
    )
    q25 = models.IntegerField(
        label="I wanted the worker’s compensation to reflect their effort.",
        max=100,
        min=0,
    )
    # =====================================================================

    # MANAGER no discretion (no participation and negotiation conditions only)
    q26 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could not adjust the worker's bonus amount at the end of the period made me think more carefully about the worker's target.",
    )
    # MANAGER no discretion (no participation and negotiation conditions only)
    q27 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Know that I could not adjust the worker's bonus amount at the end of the period made me put more effort into setting the worker's target.",
    )
    # MANAGER no discretion ALL CONDITIONS
    q28 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could not adjust the worker's bonus amount at the end of the period made me feel more responsible for the worker's bonus outcome.",
    )
    # MANAGER no discretion (no participation and negotiation conditions only)
    q29 = models.IntegerField(
        choices=scale_options,
        widget=widgets.RadioSelectHorizontal(),
        label="Knowing that I could not adjust the worker's bonus amount at the end of the period made me feel more responsible for setting an appropiate target for the worker.",
    )

    # ========================================================================================================================

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


    # def q21_choices(self):
    #     if self.group.bonus_setting == config_constants.NO_PARTICIPATION:
    #         return [
    #             "I wanted to motivate future performance.",
    #             "I wanted to show that I appreciated the worker setting a difficult target.", # (participation and negotiation conditions only)
    #             "I wanted the worker's compensation to be fail.",
    #             "I wanted the worker to trust me.",
    #             "I wanted the worker's compensation to reflect their effort.",
    #         ]
    #     else:
    #         return [
    #             "I wanted to motivate future performance.",
    #             "I wanted the worker's compensation to be fail.",
    #             "I wanted the worker to trust me.",
    #             "I wanted the worker's compensation to reflect their effort.",
    #         ]