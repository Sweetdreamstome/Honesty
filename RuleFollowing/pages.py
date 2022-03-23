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

class Control1(Page):

    form_model = 'player'
    form_fields = ['control1']

    def is_displayed(self):

        return self.player.round_number == 1 

class Control2(Page):

    form_model = 'player'
    form_fields = ['control2']

    def is_displayed(self):

        return self.player.round_number == 1 

class Control3(Page):

    form_model = 'player'
    form_fields = ['control3']

    def is_displayed(self):

        return self.player.round_number == 1 

class Control4(Page):

    form_model = 'player'
    form_fields = ['control4']

    def is_displayed(self):

        return self.player.round_number == 1 

class Control5(Page):

    form_model = 'player'
    form_fields = ['control5']

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
    Control1,
    Control2,
    Control3,
    Control4,
    Control5,
    Game,  
    Payoffs
    ]
