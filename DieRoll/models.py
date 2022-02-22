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


doc = """
Die Rolling game
"""

class Constants(BaseConstants):
    name_in_url = 'DieRoll'
    players_per_group = None
    num_rounds = 2
    choices = [1,2,3,4,5,6]

class Subsession(BaseSubsession):
    
    def creating_session(self):
        for player in self.get_players():
            player.result = random.choice(Constants.choices)
            print(player.result)

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    result = models.IntegerField()
    
    die = models.IntegerField(
        label = 'Reporte el resultado del dado',
        choices = [1,2,3,4,5,6]
    )

    def set_payoff(self):
        self.payoff = 0 if self.die == 6 else self.die*2
