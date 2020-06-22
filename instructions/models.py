import itertools
from django.utils.translation import ugettext_lazy as _

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1
    mean_remuneration = 1400

    deferred_group = ['Deferred', 'Deferred_LowTax']
    baseline = ['Deferred', 'Immediate']

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            #treat = itertools.cycle(['Deferred', 'Immediate', 'Deferred_LowTax', 'Immediate_LowTax'])
            treat = itertools.cycle(['Deferred', 'Immediate', 'Deferred_LowTax'])
            income_plus = 200
            for p in self.get_players():
                p.participant.vars['treatment'] = next(treat)
                #p.participant.vars['treatment'] = self.session.config['treatment']
                p.participant.vars['tax_rate'] = self.session.config['tax_rate']
                p.participant.vars['test'] = self.session.config['test']
                if p.participant.vars['treatment'] == 'Immediate_LowTax':
                    p.participant.vars['income_list'] = [c(2000+income_plus), c(2500+income_plus), c(3000+income_plus), c(3500+income_plus)]
                else:
                    p.participant.vars['income_list'] = [c(2000), c(2500), c(3000), c(3500)]
                if p.participant.vars['treatment'] == 'Deferred_LowTax':
                    p.participant.vars['tax_rate_low'] = self.session.config['tax_rate_low']
                else:
                    p.participant.vars['tax_rate_low'] = self.session.config['tax_rate']
        else:
            pass




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment= models.StringField()

    gender = models.IntegerField(
        label=(_("Sind Sie weiblich, männlich oder divers?")),
        choices=[
            [0, _('Weiblich')],
            [1, _('Männlich')],
            [2, _('Divers')],
        ],
        widget = widgets.RadioSelect,
        blank=False,
        #initial=0
    )

    year_of_birth = models.IntegerField(
        min=1900,
        max=2004,
        label=_("Ich welchem Jahr wurden Sie geboren (z.B. 1962)?"),
        blank=False,
        #initial=1987,
    )

    risk = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [9, '']],
        label=_('Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?'),
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        #initial=1,  # zum testen
    )

    comprehension_question1 = models.IntegerField(
        verbose_name=_("Frage 1: Welche der folgenden Aussagen bezüglich der Vergütung am Ende der Studie ist richtig?"),
        #initial = 2,
        choices=[[0, _('Der durchschnittliche Auszahlungsbetrag aller Perioden wird am Ende der Studie vergütet.')],
                 [1, _('Der durchschnittliche Auszahlungsbetrag in der Ruhephase wird am Ende der Studie vergütet.')],
                 [2, _('Nur eine der insgesamt 24 Perioden wird am Ende der Studie vergütet.')]],
        widget=widgets.RadioSelect,
    )
    comprehension_question2 = models.IntegerField(
        verbose_name=_("Frage 2: In welchen Perioden einer Sequenz erhalten Sie ein Einkommen von uns?"),
        #initial = 0,
        choices=[[0, _('Perioden 1 bis 8.')],
                 [1, _('Perioden 9 bis 12.')],
                 [2, _('Perioden 1 bis 12.')]],
        widget=widgets.RadioSelect,
    )
    comprehension_question3 = models.IntegerField(
        verbose_name=_("Frage 3: Wie wird das Bruttoeinkommen in der Einkommensphase besteuert?"),
        #initial = 0,
        choices=[[0, _('Das Bruttoeinkommen unterliegt einer Steuer in Höhe von 40 %.')],
                 [1, _('Das Bruttoeinkommen unterliegt einer Steuer in Höhe von 20 %.')],
                 [2, _('Das Bruttoeinkommen ist steuerfrei.')]],
        widget=widgets.RadioSelect,
    )
    comprehension_question4 = models.IntegerField(
        verbose_name=_("Frage 4: Wie werden die Sparbeiträge in der Einkommensphase besteuert?"),
        #initial = 0,
        choices=[[0, _('Die Sparbeiträge können steuerlich geltend gemacht werden. Dementsprechend erhalten Sie eine Steuererstattung in Höhe von 40 % der Sparbeiträge.')],
                 [1, _('Die Sparbeiträge können steuerlich nicht geltend gemacht werden. Dementsprechend erhalten Sie keine Steuererstattung.')]],
        widget=widgets.RadioSelect,
    )
    comprehension_question5 = models.IntegerField(
        verbose_name=_("Frage 5: Wie wird das aus den Sparbeiträgen resultierende Bruttoeinkommen in der Ruhephase besteuert?"),
        #initial = 1,
        choices=[[0, _('Das Bruttoeinkommen in der Ruhephase ist steuerfrei.')],
                 [1, _('Das Bruttoeinkommen in der Ruhephase unterliegt einer Steuer in Höhe von 40 %.')]],
        widget=widgets.RadioSelect,
    )
    comprehension_question5_2 = models.IntegerField(
        verbose_name=_("Frage 5: Wie wird das aus den Sparbeiträgen resultierende Bruttoeinkommen in der Ruhephase besteuert?"),
        #initial = 1,
        choices=[[0, _('Das Bruttoeinkommen in der Ruhephase ist steuerfrei.')],
                 [1, _('Das Bruttoeinkommen in der Ruhephase unterliegt einer Steuer in Höhe von 25 %.')]],
        widget=widgets.RadioSelect,
    )
    comprehension_question6 = models.IntegerField(
        verbose_name=_("Frage 6: Nehmen Sie an, Sie sparen in den gesamten acht Perioden der Einkommensphase nichts und am Ende der "
                     "Studie wird eine Periode der Ruhephase ausgezahlt. Wie hoch ist dann Ihre Auszahlung in einer Periode der Ruhephase?"),
        #initial = 0,
        choices=[[0, _('Null Euro.')],
                 [1, _('Die Höhe der Steuererstattungen der Perioden 1 bis 8.')]],
        widget=widgets.RadioSelect,
    )



    wrong_answer1 = models.IntegerField(initial=0)
    wrong_answer2 = models.IntegerField(initial=0)
    wrong_answer3 = models.IntegerField(initial=0)
    wrong_answer4 = models.IntegerField(initial=0)
    wrong_answer5 = models.IntegerField(initial=0)
    wrong_answer6 = models.IntegerField(initial=0)
#    wrong_answer7 = models.IntegerField(initial=0)

    def vars_for_template(self):
        return dict(
            tax_rate = self.participant.vars['tax_rate'] * 100,
            tax_rate_low=self.participant.vars['tax_rate_low']*100,
            treatment = self.participant.vars['treatment'],
            deferred_group = Constants.deferred_group,
            test=self.participant.vars['test'],
            participation_fee= self.session.config['participation_fee'],
            payoff_e= c(1000).to_real_world_currency(self.session),
        )

#import logging
# Get an instance of a logger
#logger = logging.getLogger(__name__)