import random

from otree.api import *

from . import models


author = 'Your name here'
doc = """
Your app description
"""
# Methods:
def make_field9(label):
    return models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [9, '']],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        # initial=1, #zum testen
    )


def make_field3(label):
    return models.IntegerField(
        choices=[[1, ''], [2, ''], [3, '']],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        # initial=1, #zum testen
    )


def make_field6(label):
    return models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, '']],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        # initial=1, #zum testen
    )


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    anmerkungen = models.LongStringField(
        blank=True,
        label='Falls ja, dann schreiben Sie die Punkte bitte auf:',
    )
    erklaerung = models.LongStringField(
        blank=True,
        label='Bitte erklären',
    )
    gender = models.IntegerField(
        label=("Sind Sie weiblich, männlich oder divers?"),
        choices=[
            [0, 'Weiblich'],
            [1, 'Männlich'],
            [2, 'Divers'],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0
    )
    age = models.IntegerField(
        min=18,
        max=99,
        label="Wie alt sind Sie?",
        blank=False,
        # initial=55,
    )
    abschluss = models.IntegerField(
        label=("Was ist Ihr höchster erreichter Bildungsabschluss?"),
        choices=[
            [1, 'Hauptschulabschluss'],
            [2, 'Realschulabschluss'],
            [3, 'Abitur'],
            [4, 'Berufsausbildung'],
            [5, 'Fachhochschulabschluss'],
            [6, 'Universitätsabschluss'],
            [7, 'Duale Hochschule / Berufsakademie'],
            [8, 'Promotion'],
        ],
        blank=False,
        # initial=1,
    )
    familie = models.IntegerField(
        label=("Wie ist Ihr Familienstand?"),
        choices=[
            [1, 'Verheiratet/Lebenspartnerschaft'],
            [2, 'Ledig'],
            [3, 'Geschieden/Verwitwet'],
        ],
        blank=False,
        # initial=1,
    )
    kinder = models.IntegerField(
        label=("Haben Sie Kinder?"),
        choices=[
            [1, 'Ja'],
            [0, 'Nein'],
        ],
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        # initial=0,
    )
    income = models.IntegerField(
        label=("Wie hoch ist Ihr persönliches monatliches Nettoeinkommen nach Abzug von Steuern und Sozialversicherungen?"),
        choices=[
            [1, 'unter 500 €'],
            [2, '500 € - 1.000 €'],
            [3, '1.000 € - 1.500 €'],
            [4, '1.500 € - 2.000 €'],
            [5, '2.000 € - 2.500 €'],
            [6, '2.500 € - 3.000 €'],
            [7, '3.000 € - 3.500 €'],
            [8, '3.500 € - 4.000 €'],
            [9, '4.000 € - 4.500 €'],
            [10, '4.500 € - 5.000 €'],
            [11, '5.000 € - 5.500 €'],
            [12, '5.500 € - 6.000 €'],
            [13, '6.000 € und mehr'],
        ],
        blank=False,
        # initial=1,
    )
    fakultaet = models.IntegerField(
        label=("An welcher Fakultät sind Sie eingeschrieben?"),
        choices=[
            [0, 'Architektur und Landschaft'],
            [1, 'Bauingenieurwesen und Geodäsie'],
            [2, 'Elektrotechnik und Informatik'],
            [3, 'Jura'],
            [4, 'Maschinenbau'],
            [5, 'Mathematik und Physik'],
            [6, 'Naturwissenschaften'],
            [7, 'Philosophie'],
            [8, 'Wirtschaftswissenschaften/BWL'],
            [9, 'Sonstiges'],
            [10, 'Ich bin kein/e Student/in'],
        ],
        blank=False,
    )
    # Kontrollfragen
    kenntnis = make_field9('Wie würden Sie Ihre eigenen Steuerrechtskenntnisse einschätzen?')
    geldanlagen = make_field9(
        'Wie schätzen Sie Ihre eigenen Kenntnisse bezüglich Geldanlagen ein?'
    )
    risiko_allgemein = make_field9(
            'Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?'
    )
    risiko = make_field9(
            'Wie schätzen Sie sich persönlich ein: Sind Sie bezüglich Geldanlagen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?'
    )
    schlupf = make_field9(
            'Wie beurteilen Sie Folgendes: „Legale Steuerschlupflöcher ausnutzen, wenn man die Möglichkeit hat, ist …“'
    )
    hinterziehen = make_field9(
            'Wie beurteilen Sie Folgendes: „Steuern hinterziehen, wenn man die Möglichkeit hat, ist …“'
    )
    leistungen = make_field9(
            'Vergleichen Sie einmal das, was Sie an Steuern zahlen, mit dem, was Sie vom Staat in Form von Leistungen zurückbekommen. Wie würden Sie Ihre persönliche Lage dann beurteilen?'
    )
    sinnvoll = make_field9(
            'Würden Sie der folgenden Aussage zustimmen: Der Staat verwendet meine Steuern überwiegend für sinnvolle Ausgaben?'
    )
    handelsblatt = make_field6('Handelsblatt')
    bild = make_field6('Bild')
    spiegel = make_field6('Spiegel')
    welt = make_field6('Welt')
    zeit = make_field6('Zeit')
    focus = make_field6('Focus')
    mm = make_field6('Manager Magazin')
    regio = make_field6('Regionale Tageszeitung')
    sonsZ = make_field6('Sonstige')
    sparen = make_field9(
        'Meine Möglichkeiten Steuern zu sparen, sind im Vergleich zu anderen gerecht.'
    )
    verteilung = make_field9(
        'Das deutsche Steuersystem verteilt die Steuerlast auf alle Steuerzahler/innen gerecht.'
    )
    umgebung_hint = make_field9(
            'Die Menschen in meiner Umgebung würden es stark missbilligen, wenn sie erfahren würden, dass ich meine Steuern hinterzogen habe.'
    )
    umgebung_schl = make_field9(
            'Die Menschen in meiner Umgebung würden es stark missbilligen, wenn sie erfahren würden, dass ich legale Steuerschlupflöcher genutzt habe.'
    )
    akzeptanz_hint = make_field9('Die Deutschen akzeptieren Steuerhinterziehung nicht.')
    akzeptanz_schl = make_field9(
        'Die Deutschen akzeptieren das Ausnutzen von legalen Steuerschlupflöchern nicht.'
    )
    aufdeckung = make_field9(
            'Die deutschen Finanzämter sind in der Lage, Steuerhinterziehung mit sehr hoher Wahrscheinlichkeit aufzudecken.'
    )
    interpretation = make_field9(
            'Die deutschen Finanzämter interpretieren das Steuerrecht in einer Art und Weise, die es den Finanzämtern ermöglicht, möglichst viele Steuernachzahlungen zu erhalten und Strafen zu verhängen.'
    )
    respekt = make_field9('Die Finanzämter behandeln die Bürger mit Respekt.')
    fair = make_field9('Die Finanzämter behandeln alle fair.')
    hybrid = make_field3('Gestaltung mit hybrider Gesellschaft')
    lizenz = make_field3(
        'Nutzung von Lizenzvereinbarungen ("Double Irish with a Dutch Sandwich")'
    )
    privilegien = make_field3('Nutzung ausländischer Steuerprivilegien')
    oase = make_field3('Gewinnverschiebung in Steueroasen')
    treaty = make_field3('Treaty Shopping')
    politik = make_field9(
            'Wenn von Politik die Rede ist, hört man immer die Begriffe „links“ und „rechts“. Wo würden Sie Ihre politischen Ansichten einordnen?'
    )
    # risk = make_field9(_('Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?'))
    taxmoral = make_field9(
            'Bitte geben Sie an, ob Sie es in Ordnung finden, Steuern zu hinterziehen, wenn man die Möglichkeit dazu hat.'
    )
    taxaversion = make_field9('Wie wichtig ist es Ihnen persönlich Steuern zu sparen?')
    taxaversion2 = models.IntegerField(
        label=(
                "Stellen Sie sich bitte nun vor, Sie erben Geld und planen dies zu investieren. Ihnen werden zwei Sparprodukte angeboten."
                "Bei dem ersten Sparprodukt erhalten Sie jedes Jahr 401 €, müssen aber gleichzeitig jährlich 100 € Steuern zahlen."
                "Bei dem zweiten Sparprodukt ist die Rendite geringer, 300 € jährlich, aber dafür steuerfrei. Für welches Sparprodukt würden Sie sich entscheiden?"
        ),
        widget=widgets.RadioSelect,
        blank=False,
        # initial=1,
    )
    strafen = models.IntegerField(
        label=("Die Strafen für Steuerhinterziehung in Deutschland sind ..."),
        widget=widgets.RadioSelect,
        blank=False,
        # initial=1,
    )
    aktien = models.IntegerField(
        label=("Haben Sie schon einmal selbst Aktien oder Aktienfonds gekauft?"),
        widget=widgets.RadioSelect,
        blank=False,
        # initial=1,
    )
    dread1 = models.IntegerField(
        blank=False,
        # initial=500,
        label='1.000 € Verlust in 24 Stunden',
    )
    dread2 = models.IntegerField(
        blank=False,
        # initial=500,
        label='1.000 € Verlust in einem Jahr',
    )
    dread3 = models.IntegerField(
        blank=False,
        # initial=500,
        label='1.000 € Verlust in 10 Jahren',
    )
    # procrastination1 = make_field9(_('Ich erledige prinzipiell alles auf dem letzten Drücker.'))
    # procrastination2 = make_field9(_('Gewöhnlich antworte ich prompt auf verpasste Telefonanrufe.'))
    # procrastination3 = make_field9(_('Ich besorge Geburtstags- und Weihnachtsgeschenke immer erst in letzter Minute.'))
    # procrastination4 = make_field9(_('Wenn ich eine Rechnung über einen kleinen Betrag erhalte, bezahle ich diese sofort.'))
    # procrastination5 = make_field9(_('Mit der Klausurvorbereitung fange ich immer erst kurz vor den Klausuren an.'))
    # procrastination6 = make_field9(_('Ein aufmerksamer Leser klickt hier genau die Mitte an.'))
    gründung = models.IntegerField(
        label=(
                "Würden Sie die Möglichkeit der Gründung einer Finanzierungs- und Patentverwertungsgesellschaft in einem Niedrigsteuerland nutzen, wenn Steuerrechtsexperten dies übereinstimmend als legal einstufen?"
        ),
        choices=[
            [1, 'Ja'],
            [0, 'Nein'],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0,
    )
    aufwand = models.IntegerField(
        label=(
                "Würden Sie die Möglichkeit nutzen, denselben Aufwand in mehreren Ländern steuermindernd anzusetzen, wenn Steuerrechtsexperten dies übereinstimmend als legal einstufen?"
        ),
        choices=[
            [1, 'Ja'],
            [0, 'Nein'],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0,
    )
    doppelt = models.IntegerField(
        label=(
                "Würden Sie die Möglichkeit nutzen, sich eine Steuer doppelt erstatten zu lassen, wenn Steuerrechtsexperten dies übereinstimmend als legal einstufen?"
        ),
        choices=[
            [1, 'Ja'],
            [0, 'Nein'],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0,
    )
    kinderarbeit = models.IntegerField(
        label=(
                "Würden Sie die Möglichkeit nutzen, Kinder in Ihrem Unternehmen zu beschäftigen, wenn Sie hieraus wesentliche Einsparungen erzielen könnten?"
        ),
        choices=[
            [1, 'Ja'],
            [0, 'Nein'],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0,
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.participant.vars['test'] = subsession.session.config['test']


def vars_for_template(player: Player):
    return dict(
        # test=self.participant.vars['test'],
        # image_path12_questionnaire=_('graphics/12_periods/LifeCycle_Questionnaire.png').format(self.round_number),
    )


# PAGES
class questions1(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'abschluss', 'fakultaet', 'familie', 'kinder', 'income']

    @staticmethod
    def vars_for_template(player: Player):
        context = vars_for_template(player)
        return context


class questions2(Page):
    form_model = 'player'
    # form_fields = ['taxcomplexity', 'taxaversion2', 'procrastination1', 'procrastination2', 'procrastination3', 'procrastination4', 'procrastination5', 'procrastination6']
    form_fields = [
        'kenntnis',
        'geldanlagen',
        'risiko_allgemein',
        'risiko',
        'schlupf',
        'hinterziehen',
        'leistungen',
        'sinnvoll',
        'hybrid',
        'lizenz',
        'privilegien',
        'oase',
        'treaty',
        'handelsblatt',
        'bild',
        'spiegel',
        'welt',
        'zeit',
        'focus',
        'mm',
        'regio',
        'sonsZ',
        'sparen',
        'verteilung',
        'umgebung_hint',
        'umgebung_schl',
        'akzeptanz_hint',
        'akzeptanz_schl',
        'aufdeckung',
        'interpretation',
        'respekt',
        'fair',
        'strafen',
        'aktien',
        'politik',
    ]

    @staticmethod
    def taxaversion2_choices(player: Player):
        choices = [
            [0, _('Ich würde das Geld in das zweite Sparprodukt investieren.')],
            [1, _('Ich würde das Geld in das erste Sparprodukt investieren.')],
        ]
        random.shuffle(choices)
        return choices

    @staticmethod
    def strafen_choices(player: Player):
        choices = [
            [0, _('... viel zu niedrig.')],
            [1, _('... zu niedrig.')],
            [2, _('... etwas zu niedrig.')],
            [3, _('... angemessen.')],
            [4, _('... etwas zu hoch.')],
            [5, _('... zu hoch.')],
            [6, _('... viel zu hoch.')],
        ]
        return choices

    @staticmethod
    def aktien_choices(player: Player):
        choices = [
            [0, _('ja')],
            [1, _('nein')],
        ]
        return choices

    @staticmethod
    def kenntnis_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def geldanlagen_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def risiko_allgemein_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def risiko_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def schlupf_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def hinterziehen_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def leistungen_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def sinnvoll_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def handelsblatt_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def bild_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def spiegel_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def welt_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def zeit_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def focus_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def mm_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def regio_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def sonsZ_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def sparen_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def verteilung_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def umgebung_hint_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def umgebung_schl_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def akzeptanz_hint_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def akzeptanz_schl_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def aufdeckung_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def interpretation_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def respekt_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def fair_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def hybrid_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def lizenz_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def privilegien_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def oase_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def treaty_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def politik_error_message(player: Player, value):
        if value == None:
            return _("Diese Frage wurde nicht beantwortet.")

    @staticmethod
    def vars_for_template(player: Player):
        context = vars_for_template(player)
        return context


class questions3(Page):
    form_model = 'player'
    form_fields = ['gründung', 'aufwand', 'doppelt', 'kinderarbeit']

    @staticmethod
    def gründung_choices(player: Player):
        choices = [
            [0, _('ja')],
            [1, _('nein')],
        ]
        return choices

    @staticmethod
    def aufwand_choices(player: Player):
        choices = [
            [0, _('ja')],
            [1, _('nein')],
        ]
        return choices

    @staticmethod
    def doppelt_choices(player: Player):
        choices = [
            [0, _('ja')],
            [1, _('nein')],
        ]
        return choices

    @staticmethod
    def kinderarbeit_choices(player: Player):
        choices = [
            [0, _('ja')],
            [1, _('nein')],
        ]
        return choices


class questions4(Page):
    form_model = 'player'
    form_fields = ['erklaerung', 'anmerkungen']


class Endbildschirm(Page):
    pass


# class payment(Page):
#    form_model = 'player'
#    form_fields = ['anmerkungen']
#
#    def vars_for_template(self):
#        context =  vars_for_template(self.player)
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
    # payment,
]
