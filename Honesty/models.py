from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Honesty'
    players_per_group = 2
    num_rounds = 2
    comportamiento = ['Miente','No miente']
    grupo_asignado = ['A','B']
    tratamientos = ['Time Delay','Time Pressure']


class Subsession(BaseSubsession):
    
    def creating_session(self):

        if self.round_number == 1: 
        
            self.group_randomly()
            print(self.get_group_matrix())

        else: 
        
            self.group_like_round(1)

        tratamientos_lista = Constants.tratamientos.copy()
        for group, tratamiento in zip(self.get_groups(), tratamientos_lista):
                group.treatment = tratamiento
                print(group.treatment)

        # for player in self.get_players():
        #     lista = Constants.grupo_asignado.copy()
        #     random.shuffle(lista)
        #     player.participant.grupo_asignado = lista[0]
        #     print(player.participant.grupo_asignado)
        
class Group(BaseGroup):
    
    treatment = models.StringField(
        doc = 'tratamiento'
    )

class Player(BasePlayer):

    # grupo_asignado = models.StringField(
    #     doc = 'Grupo al fue asignado',
    # )
    
    decision = models.StringField(
        widget = widgets.RadioSelect,
        choices = Constants.grupo_asignado
    )

    comportamiento = models.StringField(
        doc='Miente o no miente'
    )

    def other_player(self):

        print(self.get_other_in_group())
        return self.get_others_in_group()[0]

    def set_payoff(self):

        if self.decision == self.participant.grupo_asignado:
            self.comportamiento = Constants.grupo_asignado[0]
        else:
            self.comportamiento = Constants.grupo_asignado[1]

        payoff_matrix = {
            'Miente':
                {
                    'Miente': [13,13],
                    'No miente': [13,8]
                },
            'No miente':
                {
                    'Miente': [8,13],
                    'No miente': [10,10]
                }
        }

        self.payoff = payoff_matrix[self.comportamiento][self.other_player().comportamiento]

        #randomizando el payoff obtenido
        random_round = random.randint(1,Constants.num_rounds)

        self.participant.payoff = self.inround(random_round).payoff


