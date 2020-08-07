from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils.translation import ugettext_lazy as _
import random

class questions1(Page):
    form_model = 'player'
    form_fields = ['gender','age', 'abschluss', 'fakultaet', 'familie', 'kinder', 'income']

    def vars_for_template(self):
        context =  self.player.vars_for_template()
        return context

class questions2(Page):
    form_model = 'player'
    #form_fields = ['taxcomplexity', 'taxaversion2', 'procrastination1', 'procrastination2', 'procrastination3', 'procrastination4', 'procrastination5', 'procrastination6']
    form_fields = ['kenntnis', 'geldanlagen', 'risiko', 'schlupf', 'hinterziehen', 'leistungen', 'sinnvoll', 'strafen', 'taxaversion2', 'taxmoral', 'taxaversion', 'dread1', 'dread2', 'dread3']

    def taxaversion2_choices(self):
        choices=[
            [0, _('Ich würde das Geld in das zweite Sparprodukt investieren.')],
            [1, _('Ich würde das Geld in das erste Sparprodukt investieren.')],
        ]
        random.shuffle(choices)
        return choices

    def strafen_choices(self):
        choices=[
            [0, _('... viel zu niedrig.')],
            [1, _('... zu niedrig.')],
            [2, _('... etwas zu niedrig.')],
            [3, _('... angemessen.')],
            [4, _('... etwas zu hoch.')],
            [5, _('... zu hoch.')],
            [6, _('... viel zu hoch.')],
        ]
        random.shuffle(choices)
        return choices

    def kenntnis_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def geldanlagen_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def risiko_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def schlupf_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def hinterziehen_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def leistungen_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def sinnvoll_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def taxmoral_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def taxaversion_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def taxaversion2_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    def vars_for_template(self):
        context =  self.player.vars_for_template()
        return context

class questions3(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']

    def vars_for_template(self):
        context =  self.player.vars_for_template()
        return context

    def before_next_page(self):
        self.participant.vars['age'] = self.player.age

#class payment(Page):
#    form_model = 'player'
#    form_fields = ['anmerkungen']
#
#    def vars_for_template(self):
#        context =  self.player.vars_for_template()
#        context.update(
#            paying_round_seq=self.participant.vars['paying_round_seq'],
#            paying_sequence=self.participant.vars['paying_sequence'],
#            total_payoff= self.participant.payoff_plus_participation_fee(),
#            participation_fee=self.session.config['participation_fee'],
#            payoff_random_period= self.participant.payoff,
#            payoff_random_period_e=self.participant.payoff.to_real_world_currency(self.session),
#            image_path12_payoff=_('graphics/12_periods/LifeCycle_Payoff.png').format(self.round_number),
#        )
#        return context




page_sequence = [
    questions1,
    questions2,
    questions3,
    #payment,
]
