from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Instructions(Page):
    pass

class Time_Pressure(Page):

    # form_model = 'player'
    # form_fields = ['decision']

    def is_displayed(self):
        return self.group.treatment == 'Time Pressure'

    def vars_for_template(self):
        return dict(
            tratamiento = self.group.treatment
        )

class Time_Delay(Page):
    
    def is_displayed(self):
        return self.group.treatment == 'Time Delay'

    def vars_for_template(self):
        return dict(
            tratamiento = self.group.treatment
        )

class Information(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


page_sequence = [
                Instructions,
                Time_Pressure,
                Time_Delay
                ]
