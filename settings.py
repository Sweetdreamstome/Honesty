from os import environ

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = ['payoff_Honesty','payoff_RuleFollowing','payoff_DieRoll','payoff_measure_task','payoff_InequityList']

SESSION_CONFIGS = [

    dict(
       name='Taller',
       display_name="Taller",
       num_demo_participants=2,
       app_sequence=['initial_page','RuleFollowing','DieRoll'],
       app_names = {'RuleFollowing':'Primera','DieRoll':'Segunda'}
    ),

    dict(
       name='HonestidadaPrueba',
       display_name="HonestidadAprueba",
       num_demo_participants=12,
       app_sequence=['initial_page','Honesty','RuleFollowing','measure_task','InequityList','payments'],
       app_names = {'Honesty':'Primera','RuleFollowing':'Segunda','measure_task':'Tercera','InequityList':'Cuarta'},
       participant_fee = SESSION_CONFIG_DEFAULTS["participation_fee"]
    ),

    dict(
       name='RuleFollowing',
       display_name="RuleFollowing",
       num_demo_participants=2,
       app_sequence=['RuleFollowing']
    ),

    dict(
       name='tanaka2010',
       display_name="Tanaka",
       num_demo_participants=2,
       app_sequence=['measure_task']
    ),
    dict(
       name='DieRoll',
       display_name="DieRoll",
       num_demo_participants=2,
       app_sequence=['DieRoll']
    ),
    dict(
       name='InequityList',
       display_name="InequityList",
       num_demo_participants=2,
       app_sequence=['InequityList']
    ),
    dict(
       name='payments',
       display_name="payments",
       num_demo_participants=2,
       app_sequence=['payments']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
        name='e2labup',
        display_name='E2LabUP - Room para sesiones online',
        participant_label_file='_rooms/e2labup-room.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2o8v%ejs+*dx7oii07kq2^$^!2ge68neft5()@go@ysky6bs47'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

DEBUG = True
