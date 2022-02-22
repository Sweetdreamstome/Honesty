from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones(Page):
    
    def is_displayed(self):
        return self.player.round_number == 1

class Roll(Page):

    timeout_seconds = 3
    timer_text = 'Die rolling.......'

class Decision(Page):

    form_model = 'player'
    form_fields = [
        'die'
    ]

    def vars_for_template(self):

        return dict(
            result = self.player.result
        )

    def before_next_page(self):
        self.player.set_payoff()

class Results(Page):
    
    def vars_for_template(self):

        return dict(
            payoff = self.player.payoff,
            resultado = self.player.result,
            die = self.player.die
        )

page_sequence = [
                Instrucciones,
                Roll,
                Decision,
                Results
                 ]
