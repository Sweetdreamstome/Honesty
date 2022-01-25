from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Game(Page):
    pass

class Instructions(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass

class Payoffs(Page):
    pass


page_sequence = [
    Game,
    Instructions, 
    ResultsWaitPage, 
    Payoffs
    ]
