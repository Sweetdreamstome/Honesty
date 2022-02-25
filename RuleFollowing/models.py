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

doc = """

Concurso de Investigacion

Grecia & Sergio

Rule Following App

"""


class Constants(BaseConstants):
    name_in_url = 'RuleFollowing'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    blue_balls = models.IntegerField(
        label = "Cantidad de pelotas en la canasta azul",
    )

    yellow_balls = models.IntegerField(
        label = "Cantidad de pelotas en la canasta amarilla",
    )

    pay_blue = models.FloatField()
    pay_yellow = models.FloatField()

    def set_payoff(self):

        self.payoff = round(self.pay_blue + self.pay_yellow,2)
        self.participant.vars['payoff_RuleFollowing'] = self.payoff
