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

    # def vars_for_template(self):
    #     return dict(
    #         color = random.shuffle(['blue','yellow'])
    #     )

    def before_next_page(self):
        self.player.set_payoff()

# class Processing(Page):

#     timeout_seconds = 1

#     def before_next_page(self):
#         self.player.set_payoff()

class Payoffs(Page):
    
    def vars_for_template(self):
        return dict(
            pay_blue = self.player.pay_blue,
            pay_yellow = self.player.pay_yellow,
            pago_final = self.player.pago_final,
            blue_balls = self.player.blue_balls,
            yellow_balls = self.player.yellow_balls,
        )

page_sequence = [
    Instructions,
    Game,  
    # Processing,
    Payoffs
    ]
