from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    
    def before_next_page(self):

        self.group.set_payoffs()

class List(Page):

    form_model = 'player'
    form_fields = ["choice"+str(i) for i in range(1,len(Constants.allocations)+1)]

class Results(Page):
    
    def vars_for_template(self):

        return dict(
            payoff = self.player.payoff
        )


page_sequence = [Instructions,List,Results]
