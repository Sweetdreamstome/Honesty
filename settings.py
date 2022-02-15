from os import environ

SESSION_CONFIGS = [
    
    dict(
       name='HonestidadaPrueba',
       display_name="HonestidadAprueba",
       num_demo_participants=6,
       app_sequence=['Honesty','RuleFollowing','measure_task']
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
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=5.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2o8v%ejs+*dx7oii07kq2^$^!2ge68neft5()@go@ysky6bs47'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
