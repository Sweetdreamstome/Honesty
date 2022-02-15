from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Game(Page):
    
    form_model = 'player'
    form_fields = [
        'blue_balls',
        'yellow_balls'
    ]

    def vars_for_template(self):
        return dict(
            color = random.shuffle(['blue','yellow'])
        )

class Instructions(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass

class Payoffs(Page):
    
    def vars_for_template(self):
        return dict(
            blue_balls = self.player.blue_balls,
            yellow_balls = self.player.yellow_balls,
        )

page_sequence = [
    Instructions,
    Game,  
    Payoffs
    ]
