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

import config_constants, config

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = 2
    num_rounds = 1

    # manager = 'manager'
    # worker = 'worker'

    manager_role = 'manager'
    worker_role = 'worker'

    general_answers = {
        'q1': True,
        'q2': True,
    }

    worker_answers = {
        'wq3': True,
        'wq4': True,
        'wq5': True,
        'wq6': True,
        'wq7': False,
        'wq8': True,
        'wq9': True,
        'wq10': True,
        'wq11': True,
        'wq12': True,
        'wq13': True,
        'wq14': True,
    }

    manager_answers = {
        'mq3': True,
        'mq4': True,
        'mq5': True,
        'mq6': True,
        'mq7': True,
        'mq8': True,
        'mq9': True,
        'mq10': True,
        'mq11': True,
        'mq12': True,
        'mq13': True,
        'mq14': True,
    }


class Subsession(BaseSubsession):
    
    def creating_session(self):
        players = self.get_players()

        # # set role and calculate if round is difficult or not
        # for player in players:
        #     if player.participant.id % 2:
        #         # todo: fix this
        #         player.custom_role = 'manager'
        #         pass
        #     else:
        #         player.custom_role = 'worker'
        #     player.participant.vars['custom_role'] = player.custom_role



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    custom_role = models.StringField()
    # ===============================================
    q1 = models.BooleanField(
        choices=[True, False],
        label="Participants will be assigned to roles of either WORKER or MANAGER."
    )
    q2 = models.BooleanField(
        choices=[True, False],
        label="A worker will be paired with a manager for a period and will be rematched with a different manager before each period."
    )
    # ===============================================
    wq3 = models.BooleanField(
        choices=[True, False],
        label="A normal period will consist of decoding one assigned number per grid, and a difficult period will consist of decoding two assigned numbers per grid."
    )
    wq4 = models.BooleanField(
        choices=[True, False],
        label=f"Each production period has an 80% chance of being a normal period and a 20% chance of being a difficult period, determined randomly by the computer."
    )
    wq5 = models.BooleanField(
        choices=[True, False],
        label=f"At the end of each period, the manager will learn whether the period was a normal or difficult period."
    )
    # ===========================================
    wq6 = models.BooleanField(
        choices=[True, False],
        label="The manager will receive 10 Lira for every grid I correctly submit."
    )
    wq7 = models.BooleanField(
        choices=[True, False],
        label="I will receive 0 Lira for every grid I correctly submit."
    )
    
    if config.bonus_setting == config_constants.NO_PARTICIPATION:
        wq8 = models.BooleanField(
            choices=[True, False],
            label="Before each period begins, the manager will set a performance target for me."
        )

    if config.bonus_setting == config_constants.PARTICIPATION:
        wq9 = models.BooleanField(
            choices=[True, False],
            label="Before each period begins, I will set a performance target for myself."
        )

    if config.bonus_setting == config_constants.NEGOTIATION:
        wq10 = models.BooleanField(
            choices=[True, False],
            label="Before each period begins, the manager and I will negotiate a performance target for me."
        )

    wq11 = models.BooleanField(
        choices=[True, False],
        label="If I achieve my target, I will be eligible to receive the standard bonus of 200 Lira."
    )

    if config.discretion:
        wq12 = models.BooleanField(
            choices=[True, False],
            label="The manager will have discretion over the actual amount of my bonus."
        )

    wq13 = models.BooleanField(
        choices=[True, False],
        label=f"10% of any awarded bonus will be paid from the earnings of the manager."
    )
    wq14 = models.BooleanField(
        choices=[True, False],
        label=f"The manager will not perform the decoding task."
    )
    # ================================================================
    mq3 = models.BooleanField(
        choices=[True, False],
        label=f"A normal period will consist of the worker decoding one assigned number per grid, and a difficult period will consist of the worker decoding two assigned numbers per grid."
    )
    mq4 = models.BooleanField(
        choices=[True, False],
        label=f"Each production period has an 80% chance of being a normal period and a 20% chance of being a difficult period, determined randomly by the computer."
    )
    mq5 = models.BooleanField(
        choices=[True, False],
        label=f"At the end of each period, I will learn whether the period was a normal or difficult period."
    )
    # ================================================================
    mq6 = models.BooleanField(
        choices=[True, False],
        label="The worker will receive 0 Lira for every grid he/she correctly submits."
    )
    mq6 = models.BooleanField(
        choices=[True, False],
        label="I will receive 10 Lira for every grid the worker correctly submits."
    )
    
    if config.bonus_setting == config_constants.NEGOTIATION:
        mq7 = models.BooleanField(
            choices=[True, False],
            label="Before each period begins, I will set a performance target for the worker."
        )

    if config.bonus_setting == config_constants.PARTICIPATION:
        mq8 = models.BooleanField(
            choices=[True, False],
            label="Before each period begins, the worker will set a performance target for him or herself."
        )

    if config.bonus_setting == config_constants.NEGOTIATION:
        mq9 = models.BooleanField(
            choices=[True, False],
            label="Before each period begins, the worker and I will negotiate a performance target for the worker."
        )

    mq10 = models.BooleanField(
        choices=[True, False],
        label="If the worker achieves the target, the worker will be eligible to receive the standard bonus of 200 Lira."
    )

    if config.discretion:
        mq11 = models.BooleanField(
            choices=[True, False],
            label="I will have discretion over the actual amount of the worker’s bonus."
        )

    mq12 = models.BooleanField(
        choices=[True, False],
        label=f"I will pay 10% of any awarded bonus to the worker from my own earnings."
    )