from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones(Page):
    
    def is_displayed(self):
        return self.player.round_number == 1

class Roll(Page):

    form_model = 'player'
    form_fields = [
        'die_report'
    ]

    def vars_for_template(self):

        return dict(
           die_result = self.player.die_result
        )

    def before_next_page(self):
        self.player.set_payoff()

class Results(Page):

    def is_displayed(self):
        return self.player.round_number == 2
    
    def vars_for_template(self):

        report_round = self.player.in_previous_rounds()[-1]

        return dict(
            payoff = report_round.payoff,
            resultado = report_round.die_result,
            die = report_round.die_report
        )

class General_results(Page):

    def is_displayed(self):
        return self.player.round_number == 2

    def vars_for_template(self):

        payoffs = {self.session.config['app_names'][app]:self.player.participant.vars['payoff_'+app] for app in self.session.config['app_sequence']}

        return dict(
            payoffs = payoffs 
        )

page_sequence = [
                Instrucciones,
                Roll,
                Results,
                General_results
                 ]
