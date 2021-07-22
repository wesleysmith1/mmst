from os import environ


SESSION_CONFIGS = [
    dict(
        name='main_experiment',
        display_name='full experiment',
        num_demo_participants=2,
        app_sequence=['instructions', 'practice', 'main', 'survey', 'payment'],
    ),
    dict(
        name='consent',
        display_name='Consent',
        num_demo_participants=1,
        app_sequence=['consent',],
    ),
    dict(
        name='survey',
        display_name='survey',
        num_demo_participants=2,
        app_sequence=['survey']
    ),
    dict(
        name='instructions',
        display_name='instructions',
        num_demo_participants=2,
        app_sequence=['instructions',]
    ),
    dict(
        name='practice',
        display_name='practice',
        num_demo_participants=2,
        app_sequence=['practice'],
    ),
    dict(
        name='main',
        display_name='game',
        num_demo_participants=2,
        app_sequence=['main'],
    ),
    dict(
        name='payment',
        display_name='payment',
        num_demo_participants=1,
        app_sequence=['payment']
    ),
    dict(
        name='pilot',
        display_name='full pilot',
        num_demo_participants=1,
        app_sequence=['pilot_instructions', 'pilot_practice', 'pilot', 'pilot_survey', 'pilot_payment']
    ),
    dict(
        name='pilot_instructions',
        display_name='pilot instructions',
        num_demo_participants=1,
        app_sequence=['pilot_instructions',]
    ),
    dict(
        name='pilot_practice',
        display_name='pilot practice',
        num_demo_participants=1,
        app_sequence=['pilot_practice',]
    ),
    dict(
        name='pilot_survey',
        num_demo_participants=1,
        display_name='pilot survey',
        app_sequence=['pilot_survey']
    ),
    dict(
        name='pilot_payment',
        num_demo_participants=1,
        display_name='pilot payment',
        app_sequence=['pilot_payment']
    )
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
