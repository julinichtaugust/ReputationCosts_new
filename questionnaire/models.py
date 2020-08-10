from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _

author = 'Your name here'

doc = """
Your app description
"""



#Methods:
def make_field9(label):
    return models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''],[4, ''], [5, ''], [6, ''],[7, ''], [8, ''], [9, '']],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        #initial=1, #zum testen
    )

def make_field3(label):
    return models.IntegerField(
        choices=[[1, ''], [2, ''], [3, '']],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        #initial=1, #zum testen
    )

def make_field6(label):
    return models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''],[4, ''], [5, ''], [6, '']],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        #initial=1, #zum testen
    )

class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = 1
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['test'] = self.session.config['test']

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
    age = models.IntegerField(
        min=18,
        max=99,
        label=_("Wie alt sind Sie?"),
        blank=False,
        #initial=55,
    )


    abschluss = models.IntegerField(
        label=(_("Was ist Ihr höchster erreichter Bildungsabschluss?")),
        choices=[
            [1, _('Hauptschulabschluss')],
            [2, _('Realschulabschluss')],
            [3, _('Abitur')],
            [4, _('Berufsausbildung')],
            [5, _('Fachhochschulabschluss')],
            [6, _('Universitätsabschluss')],
            [7, _('Duale Hochschule / Berufsakademie')],
            [8, _('Promotion')],
        ],
        blank=False,
        #initial=1,
    )

    familie = models.IntegerField(
        label=(_("Wie ist Ihr Familienstand?")),
        choices=[
            [1, _('Verheiratet/Lebenspartnerschaft')],
            [2, _('Ledig')],
            [3, _('Geschieden/Verwitwet')],
        ],
        blank=False,
        #initial=1,
    )

    kinder = models.IntegerField(
        label=(_("Haben Sie Kinder?")),
        choices=[
            [1, _('Ja')],
            [0, _('Nein')],
        ],
        widget = widgets.RadioSelectHorizontal,
        blank=False,
        #initial=0,
    )
    income = models.IntegerField(
        label=(_("Wie hoch ist Ihr persönliches monatliches Nettoeinkommen nach Abzug von Steuern und Sozialversicherungen?")),
        choices=[
            [1, _('unter 500 €')],
            [2, _('500 € - 1.000 €')],
            [3, _('1.000 € - 1.500 €')],
            [4, _('1.500 € - 2.000 €')],
            [5, _('2.000 € - 2.500 €')],
            [6, _('2.500 € - 3.000 €')],
            [7, _('3.000 € - 3.500 €')],
            [8, _('3.500 € - 4.000 €')],
            [9, _('4.000 € - 4.500 €')],
            [10, _('4.500 € - 5.000 €')],
            [11, _('5.000 € - 5.500 €')],
            [12, _('5.500 € - 6.000 €')],
            [13, _('6.000 € und mehr')],
        ],
        blank=False,
        #initial=1,
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

        blank=False

    )

    #Kontrollfragen
    kenntnis = make_field9(_('Wie würden Sie Ihre eigenen Steuerrechtskenntnisse einschätzen?'))
    geldanlagen = make_field9(_('Wie schätzen Sie Ihre eigenen Kenntnisse bezüglich Geldanlagen ein?'))
    risiko_allgemein = make_field9(_('Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?'))
    risiko = make_field9(_('Wie schätzen Sie sich persönlich ein: Sind Sie bezüglich Geldanlagen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?'))
    schlupf = make_field9(_('Wie beurteilen Sie Folgendes: „Legale Steuerschlupflöcher ausnutzen, wenn man die Möglichkeit hat, ist …“'))
    hinterziehen = make_field9(_('Wie beurteilen Sie Folgendes: „Steuern hinterziehen, wenn man die Möglichkeit hat, ist …“'))
    leistungen = make_field9(_('Vergleichen Sie einmal das, was Sie an Steuern zahlen, mit dem, was Sie vom Staat in Form von Leistungen zurückbekommen. Wie würden Sie Ihre persönliche Lage dann beurteilen?'))
    sinnvoll = make_field9(_('Würden Sie der folgenden Aussage zustimmen: Der Staat verwendet meine Steuern überwiegend für sinnvolle Ausgaben?'))
    handelsblatt= make_field6(_('Handelsblatt'))
    bild = make_field6(_('Bild'))
    spiegel = make_field6(_('Spiegel'))
    welt = make_field6(_('Welt'))
    zeit= make_field6(_('Zeit'))
    focus = make_field6(_('Focus'))
    mm = make_field6(_('Manager Magazin'))
    regio = make_field6(_('Regionale Tageszeitung'))
    sonsZ = make_field6(_('Sonstige'))
    sparen= make_field9(_('Meine Möglichkeiten Steuern zu sparen, sind im Vergleich zu anderen gerecht.'))
    verteilung= make_field9(_('Das deutsche Steuersystem verteilt die Steuerlast auf alle Steuerzahler/innen gerecht.'))
    umgebung_hint= make_field9(_('Die Menschen in meiner Umgebung würden es stark missbilligen, wenn sie erfahren würden, dass ich meine Steuern hinterzogen habe.'))
    umgebung_schl= make_field9(_('Die Menschen in meiner Umgebung würden es stark missbilligen, wenn sie erfahren würden, dass ich legale Steuerschlupflöcher genutzt habe.'))
    akzeptanz_hint= make_field9(_('Die Deutschen akzeptieren Steuerhinterziehung nicht.'))
    akzeptanz_schl= make_field9(_('Die Deutschen akzeptieren das Ausnutzen von legalen Steuerschlupflöchern nicht.'))
    aufdeckung= make_field9(_('Die deutschen Finanzämter sind in der Lage, Steuerhinterziehung mit sehr hoher Wahrscheinlichkeit aufzudecken.'))
    interpretation= make_field9(_('Die deutschen Finanzämter interpretieren das Steuerrecht in einer Art und Weise, die es den Finanzämtern ermöglicht, möglichst viele Steuernachzahlungen zu erhalten und Strafen zu verhängen.'))
    respekt= make_field9(_('Die Finanzämter behandeln die Bürger mit Respekt.'))
    fair= make_field9(_('Die Finanzämter behandeln alle fair.'))
    hybrid = make_field3(_('Gestaltung mit hybrider Gesellschaft'))
    lizenz = make_field3(_('Nutzung von Lizenzvereinbarungen ("Double Irish with a Dutch Sandwich")'))
    privilegien = make_field3(_('Nutzung ausländischer Steuerprivilegien'))
    oase = make_field3(_('Gewinnverschiebung in Steueroasen'))
    treaty = make_field3(_('Treaty Shopping'))
    politik = make_field9(_('Wenn von Politik die Rede ist, hört man immer die Begriffe „links“ und „rechts“. Wo würden Sie Ihre politischen Ansichten einordnen?'))
    #risk = make_field9(_('Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?'))
    taxmoral = make_field9(_('Bitte geben Sie an, ob Sie es in Ordnung finden, Steuern zu hinterziehen, wenn man die Möglichkeit dazu hat.'))
    taxaversion = make_field9(_('Wie wichtig ist es Ihnen persönlich Steuern zu sparen?'))

    taxaversion2 = models.IntegerField(
        label=(_("Stellen Sie sich bitte nun vor, Sie erben Geld und planen dies zu investieren. Ihnen werden zwei Sparprodukte angeboten."
               "Bei dem ersten Sparprodukt erhalten Sie jedes Jahr 401 €, müssen aber gleichzeitig jährlich 100 € Steuern zahlen."
               "Bei dem zweiten Sparprodukt ist die Rendite geringer, 300 € jährlich, aber dafür steuerfrei. Für welches Sparprodukt würden Sie sich entscheiden?")),
        widget=widgets.RadioSelect,
        blank=False,
        #initial=1,
    )

    strafen = models.IntegerField(
        label=(_("Die Strafen für Steuerhinterziehung in Deutschland sind ...")),
        widget=widgets.RadioSelect,
        blank=False,
        #initial=1,
    )


    aktien = models.IntegerField(
        label=(_("Haben Sie schon einmal selbst Aktien oder Aktienfonds gekauft?")),
        widget=widgets.RadioSelect,
        blank=False,
        #initial=1,
    )

    dread1 = models.IntegerField(
        blank=False,
        #initial=500,
        label=_('1.000 € Verlust in 24 Stunden'),
    )
    dread2 = models.IntegerField(
        blank=False,
        #initial=500,
        label=_('1.000 € Verlust in einem Jahr'),
    )
    dread3 = models.IntegerField(
        blank=False,
        #initial=500,
        label=_('1.000 € Verlust in 10 Jahren'),
    )

    #procrastination1 = make_field9(_('Ich erledige prinzipiell alles auf dem letzten Drücker.'))
    #procrastination2 = make_field9(_('Gewöhnlich antworte ich prompt auf verpasste Telefonanrufe.'))
    #procrastination3 = make_field9(_('Ich besorge Geburtstags- und Weihnachtsgeschenke immer erst in letzter Minute.'))
    #procrastination4 = make_field9(_('Wenn ich eine Rechnung über einen kleinen Betrag erhalte, bezahle ich diese sofort.'))
    #procrastination5 = make_field9(_('Mit der Klausurvorbereitung fange ich immer erst kurz vor den Klausuren an.'))
    #procrastination6 = make_field9(_('Ein aufmerksamer Leser klickt hier genau die Mitte an.'))

    gründung = models.IntegerField(
        label=(_("Würden Sie die Möglichkeit der Gründung einer Finanzierungs- und Patentverwertungsgesellschaft in einem Niedrigsteuerland nutzen, wenn Steuerrechtsexperten dies übereinstimmend als legal einstufen?")),
        choices=[
            [1, _('Ja')],
            [0, _('Nein')],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0,
    )

    aufwand = models.IntegerField(
        label=(_("Würden Sie die Möglichkeit nutzen, denselben Aufwand in mehreren Ländern steuermindernd anzusetzen, wenn Steuerrechtsexperten dies übereinstimmend als legal einstufen?")),
        choices=[
            [1, _('Ja')],
            [0, _('Nein')],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0,
    )

    doppelt = models.IntegerField(
        label=(_("Würden Sie die Möglichkeit nutzen, sich eine Steuer doppelt erstatten zu lassen, wenn Steuerrechtsexperten dies übereinstimmend als legal einstufen?")),
        choices=[
            [1, _('Ja')],
            [0, _('Nein')],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0,
    )

    kinderarbeit = models.IntegerField(
        label=(_("Würden Sie die Möglichkeit nutzen, Kinder in Ihrem Unternehmen zu beschäftigen, wenn Sie hieraus wesentliche Einsparungen erzielen könnten?")),
        choices=[
            [1, _('Ja')],
            [0, _('Nein')],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        # initial=0,
    )

    def vars_for_template(self):
        return dict(
            #test=self.participant.vars['test'],
            #image_path12_questionnaire=_('graphics/12_periods/LifeCycle_Questionnaire.png').format(self.round_number),
        )
