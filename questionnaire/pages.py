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
    form_fields = ['kenntnis', 'geldanlagen', 'risiko_allgemein', 'risiko', 'schlupf', 'hinterziehen', 'leistungen', 'sinnvoll', 'hybrid', 'lizenz', 'privilegien', 'oase', 'treaty', 'handelsblatt', 'bild', 'spiegel', 'welt', 'zeit', 'focus', 'mm', 'regio', 'sonsZ', 'sparen', 'verteilung', 'umgebung_hint', 'umgebung_schl', 'akzeptanz_hint', 'akzeptanz_schl', 'aufdeckung', 'interpretation', 'respekt', 'fair', 'strafen', 'aktien', 'politik']

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
        return choices

    def aktien_choices(self):
        choices=[
            [0, _('ja')],
            [1, _('nein')],

        ]
        return choices

    def kenntnis_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def geldanlagen_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def risiko_allgemein_error_message(self, value):
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
    def handelsblatt_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def bild_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def spiegel_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def welt_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def zeit_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def focus_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def mm_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def regio_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def sonsZ_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def sparen_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def verteilung_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def umgebung_hint_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def umgebung_schl_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def akzeptanz_hint_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def akzeptanz_schl_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def aufdeckung_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def interpretation_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def respekt_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def fair_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def hybrid_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def lizenz_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def privilegien_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def oase_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def treaty_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")
    def politik_error_message(self, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    def vars_for_template(self):
        context =  self.player.vars_for_template()
        return context

class questions3(Page):
    form_model = 'player'
    form_fields = ['gründung', 'aufwand', 'doppelt', 'kinderarbeit']

    def gründung_choices(self):
        choices=[
            [0, _('ja')],
            [1, _('nein')],

        ]
        return choices

    def aufwand_choices(self):
        choices=[
            [0, _('ja')],
            [1, _('nein')],

        ]
        return choices

    def doppelt_choices(self):
        choices=[
            [0, _('ja')],
            [1, _('nein')],

        ]
        return choices

    def kinderarbeit_choices(self):
        choices=[
            [0, _('ja')],
            [1, _('nein')],

        ]
        return choices

class questions4(Page):
    form_model = 'player'
    form_fields = ['erklaerung','anmerkungen']

class Endbildschirm(Page):
    pass

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
    questions4,
    Endbildschirm,
    #payment,
]
