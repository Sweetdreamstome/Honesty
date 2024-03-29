from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Demograp(Page):

    form_model = 'player'
    form_fields = [
        'edad',
        'sexo',
        'distrito_residencia',
        'escala',
        'ciclo',
        'carrera',
        'nivel_estudios_padres',
        'participado_antes'
        ]

    def is_displayed(self):

        return self.player.round_number == 1

class StartWaitPage(WaitPage):
    pass

class General(Page):
    
    def is_displayed(self):
        
        return self.player.round_number == 1

    def vars_for_template(self):
        return dict(
            exchange_points = self.session.config['exchange_rates']['Points'],
            exchange_solex = self.session.config['exchange_rates']['Solex']
        )

class Instrucciones(Page):

    def is_displayed(self):

        return self.player.round_number == 1
    
    def vars_for_template(self):
        return dict(
            exchange_points = self.session.config['exchange_rates']['Points'],
            exchange_solex = self.session.config['exchange_rates']['Solex']
        )

class Time_Pressure(Page):

    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):

        return self.group.treatment == 'Time Pressure' and self.player.round_number < Constants.num_rounds

    def vars_for_template(self):

        return dict(

            grupo_asignado = self.player.grupo_asignado,
            tratamiento = self.group.treatment,
            sexo_pareja = self.player.get_partner_sexo()
        )

class ControlQuestions(Page):

    def is_displayed(self):

        return self.player.round_number == 1 

class Control1(Page):

    form_model = 'player'
    form_fields = ['control1','control1_answers']

    def is_displayed(self):

        return self.player.round_number == 1 

class Control2(Page):

    form_model = 'player'
    form_fields = ['control2','control2_answers']

    def is_displayed(self):

        return self.player.round_number == 1 

class Control3(Page):

    form_model = 'player'
    form_fields = ['control3','control3_answers']

    def is_displayed(self):

        return self.player.round_number == 1 

class Control4(Page):

    form_model = 'player'
    form_fields = ['control4', 'control4_answers']

    def is_displayed(self):

        return self.player.round_number == 1 

class Control5(Page):

    form_model = 'player'
    form_fields = ['control5','control5_answers']

    def is_displayed(self):

        return self.player.round_number == 1 

class Time_Delay(Page):

    form_model = 'player'
    form_fields = ['decision']
    
    def is_displayed(self):

        return self.group.treatment == 'Time Delay' and self.player.round_number < Constants.num_rounds

    def vars_for_template(self):

        return dict(

            grupo_asignado = self.player.grupo_asignado,
            tratamiento = self.group.treatment,
            sexo_pareja = self.player.get_partner_sexo()
        )

class Information_results(Page):

    def is_displayed(self):

        return self.group.treatment == 'Information' and self.player.round_number > 1

    def vars_for_template(self):

        #Obteniendo las decisiones pasadas de cada jugador en el grupo

        lista = self.player.get_others_in_group()

        filter_list = []
        count_player = 0
        for player in lista: 

            player_dic = {}

            count_player += 1
            grupo_asignado = player.in_previous_rounds()[-1].grupo_asignado
            decision = player.in_previous_rounds()[-1].decision

            player_dic = {
                'numero':count_player,
                'grupo_asignado': grupo_asignado,
                'decision':decision
            }

            filter_list.append(player_dic)

        return dict(
            player_list = filter_list,
            your_group = self.player.in_previous_rounds()[-1].grupo_asignado,
            your_decision = self.player.in_previous_rounds()[-1].decision,
            round = self.player.round_number - 1
        )

class Information_decision(Page):

    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):

        return self.group.treatment == 'Information'

    def vars_for_template(self):

        return dict(
            grupo_asignado = self.player.grupo_asignado,
            tratamiento = self.group.treatment,
            sexo_pareja = self.player.get_partner_sexo()
        )

class RoundWaitPage(Page):

    timer_text = 'En breves podrá pasar a la siguiente ronda'
    timeout_seconds = 5

class ResultsWaitPage(WaitPage):

    # Ojo que esto no espera a todos los players, solo espera a los del mismo grupo
    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.set_comportamiento()

        for player in self.group.get_players():
            player.set_payoff()
            
class Payoffs(Page):

    def is_displayed(self):

        if self.group.treatment == 'Information':

            return self.player.round_number == Constants.num_rounds

        else:

            return self.player.round_number == Constants.num_rounds - 1

    def vars_for_template(self):

        return dict(
            final_payoff = self.player.final_payoff,
            final_payoff_soles = self.player.final_payoff * self.session.config["exchange_rates"]["Points"],
            pay_round = self.player.pay_round
        )

page_sequence = [
                Demograp, #cuestionario inicial 
                StartWaitPage, #waitpage para que todos los del grupo avancen en orden
                General, #bienvenida
                Instrucciones, #instrucciones del juego (dependiendo del tratamiento)
                ControlQuestions,
                Control1,
                Control2,
                Control3,
                Control4,
                Control5,
                StartWaitPage, #para mantener el orden
                Information_results, # a partir de ronda 1
                RoundWaitPage,# no aparece en la ultima ronda
                Information_decision, 
                Time_Pressure, 
                Time_Delay,
                ResultsWaitPage, # calcula los payoff 
                Payoffs
                ]
