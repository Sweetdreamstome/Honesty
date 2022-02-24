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
   
class Subsession(BaseSubsession):
    
    def creating_session(self):
        for player in self.get_players(): 
            player.die_result = random.choice([1,2,3,4,5,6])
            print(player.die_result)

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    die_result = models.IntegerField()
    
    die_report = models.IntegerField(
        choices = [0,1,2,3,4,5,6]
    )

    def set_payoff(self):
        self.payoff = 0 if self.die_report == 6 else self.die_report*2
        if self.round_number == 2:
            self.participant.vars['payoff_DieRoll'] = self.in_previous_rounds()[-1].payoff
