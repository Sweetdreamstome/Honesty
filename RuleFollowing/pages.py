from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Instructions(Page):
    pass

class Game(Page):
    
    form_model = 'player'
    form_fields = [
        'blue_balls',
        'yellow_balls',
        'pay_blue',
        'pay_yellow'
    ]

    def vars_for_template(self):
        return dict(
            color = self.player.color_order
        )

    def before_next_page(self):
        self.player.set_payoff()

class Control(Page):

    def is_displayed(self):

        return self.player.round_number == 1 

class Payoffs(Page):
    
    def vars_for_template(self):
        return dict(
            pay_blue = self.player.pay_blue,
            pay_yellow = self.player.pay_yellow,
            pago_final = self.player.payoff,
            blue_balls = self.player.blue_balls,
            yellow_balls = self.player.yellow_balls,
        )

page_sequence = [
    Instructions,
    Control,
    Game,  
    Payoffs
    ]
