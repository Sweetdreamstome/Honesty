from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Pagos(Page):
    
    def vars_for_template(self):

        apps = self.session.config['app_names']

        pagos_apps = {}
        pago_total = 0

        for app in self.session.config['app_sequence'][1:-1]:
            name = apps[app]
            pago = self.player.participant.vars['payoff_'+app]
            
            pagos_apps[name] = pago

            pago_total += pago

        return dict(
            pagos_apps = pagos_apps,
            participant_fee = self.session.config["participant_fee"],
            pago_total = pago_total
        )

class Comments(Page):

    form_model = 'player'
    form_fields = [
        'interfaz',
        'instrucciones',
        'espera',
        'preguntas_control',
        'sugerencia'
        ]

class Gracias(Page):
    pass

page_sequence = [Pagos,Comments,Gracias]

