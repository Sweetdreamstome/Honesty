from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Initial_demograp(Page):

    form_model = 'player'
    form_fields = [
        'nombres',
        'apellido_paterno',
        'apellido_materno',
        'edad',
        'sexo',
        'participado_antes'
        ]

class StartWaitPage(WaitPage):

    def is_displayed(self):
        return (self.player.sexo + self.player.other_player().sexo) != '00'  

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
            tratamiento = self.group.treatment,
            sexo_pareja = self.player.other_player().sexo
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
            tratamiento = self.group.treatment,
            sexo_pareja = self.player.other_player().sexo
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
                Initial_demograp,
                StartWaitPage,
                Instructions,
                Time_Pressure,
                Time_Delay,
                ResultsWaitPage,
                Payoffs
                ]
