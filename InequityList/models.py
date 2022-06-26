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

    Inequity List

"""

class Constants(BaseConstants):

    name_in_url = 'InequityList'
    players_per_group = 2
    num_rounds = 1

    payments = [[20,i] for i in range(10,31)]
    allocations = [i for i in range(len(payments))]

class Subsession(BaseSubsession):
    
    def creating_session(self):

        import random 

        roles = [0,1]
        groups = self.get_groups()

        for group in groups:

            #assigning allocation to group
            group.payment_choice = random.choice(Constants.allocations)
            
            #assigning role 
            p1 , p2 = group.get_players() 
            random.shuffle(roles)
            p1.position , p2.position = roles

class Group(BaseGroup):
    
    payment_choice = models.IntegerField() #sumar 1 por cuenta propia porque esta var irá de 0 a 20 

    def set_payoffs(self):

        allocation = Constants.payments[self.payment_choice]

        p1 , p2 = self.get_players()
        p1.payoff , p2.payoff = allocation[p1.position] , allocation[p2.position] 
        p1.participant.vars["payoff_InequityList"] , p2.participant.vars["payoff_InequityList"] = p1.payoff , p2.payoff

class Player(BasePlayer):

    #0 es i y 1 es j
    position = models.IntegerField()
    
    choice1 = models.FloatField()
    choice2 = models.FloatField()
    choice3 = models.FloatField()
    choice4 = models.FloatField()
    choice5 = models.FloatField()
    choice6 = models.FloatField()
    choice7 = models.FloatField()
    choice8 = models.FloatField()
    choice9 = models.FloatField()
    choice10 = models.FloatField()
    choice11 = models.FloatField()
    choice12 = models.FloatField()
    choice13 = models.FloatField()
    choice14 = models.FloatField()
    choice15 = models.FloatField()
    choice16 = models.FloatField()
    choice17 = models.FloatField()
    choice18 = models.FloatField()
    choice19 = models.FloatField()
    choice20 = models.FloatField()
    choice21 = models.FloatField()

