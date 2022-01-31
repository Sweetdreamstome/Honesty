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


author = 'Grecia Barandiaran & Sergio Mejia '

doc = """

Concurso de Investigacion 2021

Test about Honesty 

Apps: Honesty, Rule Following & Tanaka (2010)

"""


class Constants(BaseConstants):
    name_in_url = 'Honesty'
    players_per_group = 2
    num_rounds = 2

    #constatnes del experimento
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

        assing_groups = Constants.grupo_asignado.copy()
        for group in self.get_groups():

            p1 , p2  =  group.get_players()
            random.shuffle(assing_groups)
            p1.grupo_asignado, p2.grupo_asignado = assing_groups
            print(p1.grupo_asignado,p2.grupo_asignado)
        
class Group(BaseGroup):
    
    treatment = models.StringField(
        doc = 'tratamiento'
    )

class Player(BasePlayer):

    #breve cuestionario inicial

    nombres = models.StringField(
        label = 'Indica tus nombres:'
    )

    apellido_paterno = models.StringField(
        label = 'Indica tu apellido paterno:'
    )

    apellido_materno = models.StringField(
        label = 'Indica tu apellido materno:'
    )

    edad = models.IntegerField(
        label = 'Indica tu edad:',
        choices = [i for i in range(18,40)]
    )

    #variable de interes 
    sexo = models.StringField(
        label = 'Indica tu sexo:',
        widget = widgets.RadioSelectHorizontal,
        choices = ['Hombre','Mujer'],
        default = '0'
    )

    participado_antes = models.StringField(
        label = 'Has participado antes en un experimento del E2LabUP',
        choices =['Si', 'No']
    )

    grupo_asignado = models.StringField(
    )
    
    decision = models.StringField(
        widget = widgets.RadioSelectHorizontal,
        choices = Constants.grupo_asignado
    )

    final_payoff = models.CurrencyField()

    comportamiento = models.StringField()

    def get_sexo(self):

        return self.in_round(1).sexo

    def set_comportamiento(self):
        
        print(self.decision, self.grupo_asignado)

        if self.decision == self.grupo_asignado:

            self.comportamiento = Constants.comportamiento[1]

        else:

            self.comportamiento = Constants.comportamiento[0] 

    def other_player(self):

        return self.get_others_in_group()[0]

    def set_payoff(self):

        print(self.comportamiento)
        print(self.get_others_in_group())
        print(self.round_number)
        print(self.comportamiento)

        payoff_matrix = {
            'Miente':
                {
                    'Miente': 13,
                    'No miente': 13
                },
            'No miente':
                {
                    'Miente': 8,
                    'No miente': 10
                }
        }

        self.payoff = payoff_matrix[self.comportamiento][self.other_player().comportamiento]

        print(self.payoff)

        #randomizando el payoff obtenido final
        random_round = random.randint(1,Constants.num_rounds)

        print(random_round)

        self.final_payoff = self.in_round(1).payoff #cambiar esto a aleatorio (random_round)



