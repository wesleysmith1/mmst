from os import environ

import config_constants

SESSION_CONFIGS = [
    dict(
        name='discretion_negotiation',
        display_name='Discretion & Negotiation',
        num_demo_participants=2,
        app_sequence=['instructions', 'practice', 'main', 'survey', 'payment'],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.NEGOTIATION,
        ),
    ),
    dict(
        name='discretion_participation',
        display_name='Discretion - Participation',
        num_demo_participants=2,
        app_sequence=['instructions', 'practice', 'main', 'survey', 'payment'],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.PARTICIPATION,
        ),
    ),
    dict(
        name='discretion_no_participation',
        display_name='Discretion - No Participation',
        num_demo_participants=2,
        app_sequence=['instructions', 'practice', 'main', 'survey', 'payment'],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.NO_PARTICIPATION,
        ),
    ),
    dict(
        name='no_discretion_no_participation',
        display_name='No Discretion - No Participation',
        num_demo_participants=2,
        app_sequence=['instructions', 'practice', 'main', 'survey', 'payment'],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.NO_PARTICIPATION,
        ),
    ),
    dict(
        name='no_discretion_participation',
        display_name='No Discretion - participation',
        num_demo_participants=2,
        app_sequence=['instructions', 'practice', 'main', 'survey', 'payment'],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.PARTICIPATION,
        ),
    ),
    dict(
        name='no_discretion_negotiation',
        display_name='No Discretion - Negotiation',
        num_demo_participants=2,
        app_sequence=['instructions', 'practice', 'main', 'survey', 'payment'],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.NEGOTIATION,
        ),
    ),
    # ========================surveys with treatment=================================
    dict(
        name='survey_discretion_negotiation',
        display_name='survey (discretion-negotiation)',
        num_demo_participants=2,
        app_sequence=['survey'],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.NEGOTIATION,
        ),
    ),
    dict(
        name='survey_discretion_no_participation',
        display_name='survey (discretion-no-participation)',
        num_demo_participants=2,
        app_sequence=['survey'],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.NO_PARTICIPATION,
        ),
    ),
    dict(
        name='survey_discretion_participation',
        display_name='survey (discretion-participation)',
        num_demo_participants=2,
        app_sequence=['survey'],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.PARTICIPATION,
        ),
    ),
    dict(
        name='survey_no_discretion_negotiation',
        display_name='survey (no discretion-negotiation)',
        num_demo_participants=2,
        app_sequence=['survey'],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.NEGOTIATION,
        ),
    ),
    dict(
        name='survey_no_discretion_no_participation',
        display_name='survey (no discretion-no participation)',
        num_demo_participants=2,
        app_sequence=['survey'],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.NO_PARTICIPATION,
        ),
    ),
    dict(
        name='survey_no_discretion_participation',
        display_name='survey (no discretion-participation)',
        num_demo_participants=2,
        app_sequence=['survey'],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.PARTICIPATION,
        ),
    ),
    # =================================================================
    dict(
        name='instructions_discretion_negotiation',
        display_name='Instructions (discretion-negotiation)',
        num_demo_participants=2,
        app_sequence=['instructions',],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.NEGOTIATION,
        ),
    ),
    dict(
        name='instructions_discretion_no_participation',
        display_name='Instructions (discretion-no participation)',
        num_demo_participants=2,
        app_sequence=['instructions',],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.NO_PARTICIPATION,
        ),
    ),
    dict(
        name='instructions_discretion_participation',
        display_name='Instructions (discretion-participation)',
        num_demo_participants=2,
        app_sequence=['instructions',],
        vars=dict(
            discretion=True,
            bonus_setting=config_constants.PARTICIPATION,
        ),
    ),
    dict(
        name='instructions_no_discretion_negotiation',
        display_name='Instructions (no discretion-negotiation)',
        num_demo_participants=2,
        app_sequence=['instructions',],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.NEGOTIATION,
        ),
    ),
    dict(
        name='instructions_no_discretion_no_participation',
        display_name='Instructions (no discretion-no participation)',
        num_demo_participants=2,
        app_sequence=['instructions',],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.NO_PARTICIPATION,
        ),
    ),
    dict(
        name='instructions_no_discretion_participation',
        display_name='Instructions (no discretion-participation)',
        num_demo_participants=2,
        app_sequence=['instructions',],
        vars=dict(
            discretion=False,
            bonus_setting=config_constants.PARTICIPATION,
        ),
    ),
    # dict(
    #     name='practice',
    #     display_name='practice',
    #     num_demo_participants=2,
    #     app_sequence=['practice'],
    #     vars=dict(
    #         discretion=True,
    #         bonus_setting=config_constants.NEGOTIATION,
    #     ),
    # ),
    # dict(
    #     name='main',
    #     display_name='game',
    #     num_demo_participants=2,
    #     app_sequence=['main'],
    # ),
    # dict(
    #     name='consent',
    #     display_name='Consent',
    #     num_demo_participants=1,
    #     app_sequence=['consent',],
    # ),
    # dict(
    #     name='payment',
    #     display_name='payment',
    #     num_demo_participants=1,
    #     app_sequence=['payment']
    # ),
    dict(
        name='pilot',
        display_name='full pilot',
        num_demo_participants=1,
        app_sequence=['pilot_instructions', 'pilot_practice', 'pilot', 'pilot_survey', 'pilot_payment']
    ),
    # dict(
    #     name='pilot_instructions',
    #     display_name='pilot instructions',
    #     num_demo_participants=1,
    #     app_sequence=['pilot_instructions',]
    # ),
    # dict(
    #     name='pilot_practice',
    #     display_name='pilot practice',
    #     num_demo_participants=1,
    #     app_sequence=['pilot_practice',]
    # ),
    # dict(
    #     name='pilot_survey',
    #     num_demo_participants=1,
    #     display_name='pilot survey',
    #     app_sequence=['pilot_survey']
    # ),
    # dict(
    #     name='pilot_payment',
    #     num_demo_participants=1,
    #     display_name='pilot payment',
    #     app_sequence=['pilot_payment']
    # )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=.02, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = 'n5jl026@16paq5lh@oj$n(t^^7wd%i_0bfgv-$n0r))4eov0c6'

INSTALLED_APPS = ['otree']
