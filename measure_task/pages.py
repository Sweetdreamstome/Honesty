from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class Example1(Page):
    pass


class Example2(Page):
    pass


class Example3(Page):
    pass


class Example4(Page):
    pass

class Decision1(Page):
    form_model = 'player'
    form_fields = ['first_choice_1', 'second_choice_1']

class Decision2(Page):
    form_model = 'player'
    form_fields = ['first_choice_2', 'second_choice_2']

class Decision3(Page):
    form_model = 'player'
    form_fields = ['first_choice_3', 'second_choice_3']

    def before_next_page(self):
        self.player.set_payoffs()

class Results(Page):
    
    def vars_for_template(self):
        return dict(
            pago_soles = self.player.payoff * self.session.config["exchange_rates"]["Solex"],
        )


page_sequence = [
    Introduction, Example1, Example2, Example3, Example4, 
Decision1, Decision2, Decision3, Results]
