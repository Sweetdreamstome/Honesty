from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Instructions(Page):
    pass

class Time_Pressure(Page):

    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return self.group.treatment == 'Time Pressure'

    timeout_seconds = 30

    def vars_for_template(self):
        return dict(
            grupo_asignado = self.player.grupo_asignado,
            tratamiento = self.group.treatment
        )

class Time_Delay(Page):

    form_model = 'player'
    form_fields = ['decision']
    
    def is_displayed(self):
        return self.group.treatment == 'Time Delay'

    timeout_seconds = 20    

    def vars_for_template(self):
        return dict(
            grupo_asignado = self.player.grupo_asignado,
            tratamiento = self.group.treatment
        )

#tratamiento que falta codear
class Information(Page):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.set_comportamiento()

        for player in self.group.get_players():
            player.set_payoff()
            
class Payoffs(Page):

    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):

        return dict(
            final_payoff = self.player.participant.payoff
        )


page_sequence = [
                Instructions,
                Time_Pressure,
                Time_Delay,
                ResultsWaitPage,
                Payoffs
                ]
