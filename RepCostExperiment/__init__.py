import itertools
import random

from otree.api import *


author = 'Your name here'
doc = """
Your app description 4
"""


class Constants(BaseConstants):
    name_in_url = 'RepCostExperiment'
    players_per_group = 6
    sequence_length = 12
    sequence_number = 2
    num_rounds = sequence_length * sequence_number
    diviA = [10, 20, 30, 40, 50]
    diviA_high = [20, 30, 40, 50, 60]
    diviB = [10, 20, 30, 40, 50]
    mean_remuneration = 1500
    Umsatz = 175.0
    GvS = 35.0
    GnS_low = 32.4
    GnS_high = 24.5
    ETR_low = 7.5
    ETR_high = 30.0
    Steuern_low = 2.6
    Steuern_high = 10.5
    fix = 3.00


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    marktpreisA = models.CurrencyField()
    clearing_rankA = models.IntegerField()
    dividendeA = models.CurrencyField()
    marktpreisB = models.CurrencyField()
    clearing_rankB = models.IntegerField()
    dividendeB = models.CurrencyField()
    # marktpreisA_alt = models.CurrencyField()


class Player(BasePlayer):
    rand = models.IntegerField()
    verkaufA = models.CurrencyField(blank=True)
    kaufA = models.CurrencyField(blank=True)
    endowment = models.CurrencyField(initial=1500)
    endowmentalt = models.CurrencyField()
    is_trade_kaufA = models.BooleanField(initial=False)
    is_trade_verkaufA = models.BooleanField(initial=False)
    anzahlA = models.IntegerField(initial=5)
    rank_verkaufA = models.IntegerField()
    rank_kaufA = models.IntegerField()
    gesdiviA = models.CurrencyField()
    verkaufB = models.CurrencyField(blank=True)
    kaufB = models.CurrencyField(blank=True)
    is_trade_kaufB = models.BooleanField(initial=False)
    is_trade_verkaufB = models.BooleanField(initial=False)
    anzahlB = models.IntegerField(initial=5)
    rank_verkaufB = models.IntegerField()
    rank_kaufB = models.IntegerField()
    gesdiviB = models.CurrencyField()
    treatment = models.StringField()
    auszahlung_euro_1 = models.CurrencyField(initial=0)
    auszahlung_euro_2 = models.CurrencyField(initial=0)
    endowment_euro_1 = models.CurrencyField(initial=0)
    endowment_euro_2 = models.CurrencyField(initial=0)
    endowment_ende_1 = models.CurrencyField(initial=0)
    endowment_ende_2 = models.CurrencyField(initial=0)
    payoff_1 = models.CurrencyField()
    payoff_2 = models.CurrencyField()
    gender = models.IntegerField(
        label=(("Sind Sie weiblich, männlich oder divers?")),
        choices=[
            [0, ('Weiblich')],
            [1, ('Männlich')],
            [2, ('Divers')],
        ],
        widget=widgets.RadioSelect,
        blank=False,
        initial=0,
    )
    year_of_birth = models.IntegerField(
        min=1900,
        max=2004,
        label=("Ich welchem Jahr wurden Sie geboren (z.B. 1962)?"),
        blank=False,
        initial=1987,
    )
    risk = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [9, '']],
        label=(
            'Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?'
        ),
        widget=widgets.RadioSelectHorizontal,
        blank=False,
        initial=1,  # zum testen
    )
    # comprehension_question1 = models.IntegerField(
    #    verbose_name=(
    #        "Frage 1: Welche der folgenden Aussagen bezüglich der Vergütung am Ende des Experiments ist richtig?"),
    #    initial = 2,
    #    choices=[[0, ('Das durchschnittliche Endvermögen der beiden Sequenzen wird am Ende des Experiments ausgezahlt.')],
    #             [1, ('Die Summe des gesamten Vermögens beider Sequenzen wird am Ende des Experiments ausgezahlt.')],
    #             [2, ('Nur das Endvermögen einer der zwei Sequenzen wird am Ende des Experiments vergütet.')]],
    #    widget=widgets.RadioSelect,
    # )
    comprehension_question2 = models.IntegerField(
        verbose_name=("Frage 1: Wonach bestimmt sich die Vergütung einer Sequenz?"),
        initial=0,
        choices=[
            [0, ('Nach der Höhe des Bankguthabens nach Ablauf aller Perioden einer Sequenz.')],
            [1, ('Nach der Anzahl der Aktien im Portfolio.')],
            [
                2,
                (
                    'Nach der Höhe des Bankguthabens nach Ablauf aller Perioden und nach der Anzahl der Aktien im Portfolio.'
                ),
            ],
        ],
        widget=widgets.RadioSelect,
    )
    comprehension_question3 = models.IntegerField(
        verbose_name=("Frage 2: Welches Unternehmen hat einen höheren Gewinn vor Steuern?"),
        initial=0,
        choices=[
            [0, ('Der Gewinn vor Steuern ist gleich groß.')],
            [1, ('Das A-Unternehmen hat einen höheren Gewinn vor Steuern.')],
            [2, ('Das B-Unternehmen hat einen höheren Gewinn vor Steuern.')],
        ],
        widget=widgets.RadioSelect,
    )
    comprehension_question4 = models.IntegerField(
        verbose_name=("Frage 3: Wie viele Teilnehmer (mit Ihnen) handeln auf dem Markt?"),
        initial=1,
        choices=[
            [0, ('5')],
            [1, ('6')],
            [2, ('7')],
        ],
        widget=widgets.RadioSelect,
    )
    comprehension_question5 = models.IntegerField(
        verbose_name=("Frage 4: Welches Unternehmen zahlt weniger Steuern?"),
        initial=1,
        choices=[[1, ('Das A-Unternehmen.')], [2, ('Das B-Unternehmen.')]],
        widget=widgets.RadioSelect,
    )
    comprehension_question5_2 = models.IntegerField(
        verbose_name=("Frage 4: Welches Unternehmen zahlt weniger Steuern?"),
        initial=2,
        choices=[[1, ('Das A-Unternehmen.')], [2, ('Das B-Unternehmen.')]],
        widget=widgets.RadioSelect,
    )
    comprehension_question6 = models.IntegerField(
        verbose_name=("Frage 5: Wie ändert sich Ihr Bankguthaben?"),
        initial=2,
        choices=[
            [0, ('Nur durch den Kauf oder Verkauf von Aktien.')],
            [1, ('Nur durch Dividenden, die Sie für die Aktien in ihrem Portfolio erhalten.')],
            [
                2,
                (
                    'Sowohl durch den Kauf und Verkauf von Aktien, als auch durch Dividendenzahlungen für Aktien in dem Portfolio.'
                ),
            ],
        ],
        widget=widgets.RadioSelect,
    )
    # Frage zu Anzahl Perioden
    # Frage zu Unsicherheit Dividenden
    wrong_answer1 = models.IntegerField(initial=0)
    wrong_answer2 = models.IntegerField(initial=0)
    wrong_answer3 = models.IntegerField(initial=0)
    wrong_answer4 = models.IntegerField(initial=0)
    wrong_answer5 = models.IntegerField(initial=0)
    wrong_answer5_2 = models.IntegerField(initial=0)
    wrong_answer6 = models.IntegerField(initial=0)
    #    wrong_answer7 = models.IntegerField(initial=0)


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.rand = random.choice([1, 2])
    else:
        for player in subsession.get_players():
            player.rand = player.in_round(1).rand


def func_sequence(subsession: Subsession):
    if subsession.round_number <= Constants.sequence_length:
        return 1
    else:
        return 2


def func_period(subsession: Subsession):
    if func_sequence(subsession) == 1:
        return subsession.round_number
    else:
        return subsession.round_number - Constants.sequence_length


def marktpreisA_alt(group: Group):
    if group.round_number == 1:
        pass
    else:
        return group.in_round(group.round_number - 1).marktpreisA


def marktpreisB_alt(group: Group):
    if group.round_number == 1:
        pass
    else:
        return group.in_round(group.round_number - 1).marktpreisB


# Sortierte Liste der Verkaufspreise (Angebote: von klein nach groß)
def verkaufA_liste(group: Group):
    players = group.get_players()
    for p in players:
        if p.verkaufA == 0:
            p.verkaufA = 99999
    group.verkaufA_liste = [p.verkaufA for p in players]
    group.verkaufA_liste.sort()
    return group.verkaufA_liste


def verkaufB_liste(group: Group):
    players = group.get_players()
    for p in players:
        if p.verkaufB == 0:
            p.verkaufB = 99999
    group.verkaufB_liste = [p.verkaufB for p in players]
    group.verkaufB_liste.sort()
    return group.verkaufB_liste


# Sortierte Liste der Kaufspreise (Nachfragen: von groß nach klein)
def kaufA_liste(group: Group):
    players = group.get_players()
    group.kaufA_liste = [p.kaufA for p in players]
    group.kaufA_liste.sort(reverse=True)
    return group.kaufA_liste


def kaufB_liste(group: Group):
    players = group.get_players()
    group.kaufB_liste = [p.kaufB for p in players]
    group.kaufB_liste.sort(reverse=True)
    return group.kaufB_liste




################################################################################################
def datenA_verkauf(group: Group):
    players = group.get_players()
    v = []
    w1 = 0
    for p in players:
        v.append({'SPIELER': p.id_in_group, 'ANGEBOT': p.verkaufA})
        group.datenA_verkauf = sorted(v, key=lambda k: (k['ANGEBOT'], random.random()))
    for item in group.datenA_verkauf:
        w1 = w1 + 1
        item.update({'RANK': w1})
    return group.datenA_verkauf


def datenA_kauf(group: Group):
    players = group.get_players()
    k = []
    w2 = 0
    for p in players:
        k.append({'SPIELER': p.id_in_group, 'NACHFRAGE': p.kaufA})
        group.datenA_kauf = sorted(k, key=lambda k: (k['NACHFRAGE'], random.random()), reverse=True)
    for item in group.datenA_kauf:
        w2 = w2 + 1
        item.update({'RANK': w2})
    return group.datenA_kauf


def rank_verkaufA(group: Group):
    players = group.get_players()
    datenA_verkauf = group.datenA_verkauf
    for p in players:
        for item in datenA_verkauf:
            if p.id_in_group == item['SPIELER']:
                p.rank_verkaufA = item['RANK']
            else:
                pass


def rank_kaufA(group: Group):
    players = group.get_players()
    datenA_kauf = group.datenA_kauf
    for p in players:
        for item in datenA_kauf:
            if p.id_in_group == item['SPIELER']:
                p.rank_kaufA = item['RANK']
            else:
                pass


def datenA_verkauf_liste(group: Group):
    group.datenA_verkauf_liste = [d['SPIELER'] for d in group.datenA_verkauf]


def datenA_kauf_liste(group: Group):
    group.datenA_kauf_liste = [d['SPIELER'] for d in group.datenA_kauf]


#############################################################
def datenB_verkauf(group: Group):
    players = group.get_players()
    c = []
    w3 = 0
    for p in players:
        c.append({'SPIELER': p.id_in_group, 'ANGEBOT': p.verkaufB})
        group.datenB_verkauf = sorted(c, key=lambda k: (k['ANGEBOT'], random.random()))
    for item in group.datenB_verkauf:
        w3 = w3 + 1
        item.update({'RANK': w3})
    return group.datenB_verkauf


def datenB_kauf(group: Group):
    players = group.get_players()
    h = []
    w4 = 0
    for p in players:
        h.append({'SPIELER': p.id_in_group, 'NACHFRAGE': p.kaufB})
        group.datenB_kauf = sorted(h, key=lambda k: (k['NACHFRAGE'], random.random()), reverse=True)
    for item in group.datenB_kauf:
        w4 = w4 + 1
        item.update({'RANK': w4})
    return group.datenB_kauf


def rank_verkaufB(group: Group):
    players = group.get_players()
    datenB_verkauf = group.datenB_verkauf
    for p in players:
        for item in datenB_verkauf:
            if p.id_in_group == item['SPIELER']:
                p.rank_verkaufB = item['RANK']
            else:
                pass


def rank_kaufB(group: Group):
    players = group.get_players()
    datenB_kauf = group.datenB_kauf
    for p in players:
        for item in datenB_kauf:
            if p.id_in_group == item['SPIELER']:
                p.rank_kaufB = item['RANK']
            else:
                pass


def datenB_verkauf_liste(group: Group):
    group.datenB_verkauf_liste = [d['SPIELER'] for d in group.datenB_verkauf]


def datenB_kauf_liste(group: Group):
    group.datenB_kauf_liste = [d['SPIELER'] for d in group.datenB_kauf]


###########################################
# Rank bestimmen zu dem Markt geräumt wird (Nachrage >= Angebot)
def rankA(group: Group):
    group.clearing_rankA = 0
    for i in range(1, Constants.players_per_group + 1, 1):
        a = i - 1
        if group.kaufA_liste[a] >= group.verkaufA_liste[a]:
            group.clearing_rankA = i
        else:
            pass


def rankB(group: Group):
    group.clearing_rankB = 0
    for i in range(1, Constants.players_per_group + 1, 1):
        a = i - 1
        if group.kaufB_liste[a] >= group.verkaufB_liste[a]:
            group.clearing_rankB = i
        else:
            pass


# Marktpreis in Abhänigkeit des bestimmten Ranks berechnen - Mittelwert aus Nachfrage und Angebot
def marktpreisA_rech(group: Group):
    for i in range(Constants.players_per_group, 0, -1):
        a = i - 1
        if group.clearing_rankA == i:
            group.marktpreisA = (group.kaufA_liste[a] + group.verkaufA_liste[a]) / 2
        else:
            pass


def marktpreisB_rech(group: Group):
    for i in range(Constants.players_per_group, 0, -1):
        a = i - 1
        if group.clearing_rankB == i:
            group.marktpreisB = (group.kaufB_liste[a] + group.verkaufB_liste[a]) / 2
        else:
            pass


# Jedem Spieler zuweisen, ob er ein Aktie verkauft hat oder kauft (Abfrage ob eigener Rang über "clearing" Rank
def handelA(group: Group):
    players = group.get_players()
    for p in players:
        if p.rank_kaufA <= group.clearing_rankA:
            p.is_trade_kaufA = True
        else:
            pass
        if p.rank_verkaufA <= group.clearing_rankA:
            p.is_trade_verkaufA = True
        else:
            pass


def handelB(group: Group):
    players = group.get_players()
    for p in players:
        if p.rank_kaufB <= group.clearing_rankB:
            p.is_trade_kaufB = True
        else:
            pass
        if p.rank_verkaufB <= group.clearing_rankB:
            p.is_trade_verkaufB = True
        else:
            pass


# Ausführen des Handels, in dem jedem Spieler Aktien zugerechnet und abgezogen werden, sowie die Ausstattung angepasst wird
def ausfuhrung(group: Group):
    players = group.get_players()
    for p in players:
        p.endowmentalt = p.endowment
        if p.is_trade_kaufA == True and p.is_trade_verkaufA == True:
            pass
        else:
            if p.is_trade_kaufA == True and p.is_trade_verkaufA == False:
                p.anzahlA = p.anzahlA + 1
                p.endowment = p.endowment - group.marktpreisA
            else:
                if p.is_trade_verkaufA == True and p.is_trade_kaufA == False:
                    p.anzahlA = p.anzahlA - 1
                    p.endowment = p.endowment + group.marktpreisA
                else:
                    pass
        if p.is_trade_kaufB == True and p.is_trade_verkaufB == True:
            pass
        else:
            if p.is_trade_kaufB == True and p.is_trade_verkaufB == False:
                p.anzahlB = p.anzahlB + 1
                p.endowment = p.endowment - group.marktpreisB
            else:
                if p.is_trade_verkaufB == True and p.is_trade_kaufB == False:
                    p.anzahlB = p.anzahlB - 1
                    p.endowment = p.endowment + group.marktpreisB
                else:
                    pass


# Nach Abschluss des Handels, Auszahlung der Dividende pro Aktie im neuen Portfolio
def dividende_rech(group: Group):
    group.dividendeA = c(random.choice(Constants.diviA))
    group.dividendeB = c(random.choice(Constants.diviB))
    players = group.get_players()
    for p in players:
        p.endowment = p.endowment + p.anzahlA * group.dividendeA + p.anzahlB * group.dividendeB
        p.gesdiviA = p.anzahlA * group.dividendeA
        p.gesdiviB = p.anzahlB * group.dividendeB


def set_payoffs(group: Group):
    if func_period(group.subsession) == Constants.sequence_length:
        players = group.get_players()
        if func_sequence(group.subsession) == 1:
            for p in players:
                p.payoff_1 = p.endowment
        else:
            for p in players:
                p.payoff_2 = p.endowment


def vars_for_template(player: Player):
    return dict(
        participation_fee=player.session.config['participation_fee'],
    )


# Kauf- und Verkaufspreis auf 0 setzen, falls Eingabe == None
def set_value_verkaufB(player: Player):
    if player.verkaufB == None:
        player.verkaufB = 99999
    if player.verkaufB == 0:
        player.verkaufB = 99999


def set_value_kaufB(player: Player):
    if player.kaufB == None:
        player.kaufB = 0


def set_value_verkaufA(player: Player):
    if player.verkaufA == None:
        player.verkaufA = 99999
    if player.verkaufA == 0:
        player.verkaufA = 99999


def set_value_kaufA(player: Player):
    if player.kaufA == None:
        player.kaufA = 0


# Werte der Vorperiode holen
def access_data(player: Player):
    player.endowment = player.in_round(player.round_number - 1).endowment
    player.anzahlA = player.in_round(player.round_number - 1).anzahlA
    player.anzahlB = player.in_round(player.round_number - 1).anzahlB


def access_seq_data(player: Player):
    player.payoff_1 = player.in_round(player.round_number - 1).payoff_1
    player.endowment_euro_1 = player.in_round(player.round_number - 1).endowment_euro_1
    player.auszahlung_euro_1 = player.in_round(player.round_number - 1).auszahlung_euro_1


def endowment_ende(player: Player):
    if func_sequence(player.subsession) == 1:
        player.endowment_ende_1 = player.endowment
        return player.endowment_ende_1
    else:
        player.endowment_ende_2 = player.endowment
        return player.endowment_ende_2


def endowment_euro(player: Player):
    if func_sequence(player.subsession) == 1:
        player.endowment_euro_1 = player.endowment.to_real_world_currency(player.session)
        return player.endowment_euro_1
    else:
        player.endowment_euro_1 = player.payoff_1.to_real_world_currency(player.session)
        player.endowment_euro_2 = player.endowment.to_real_world_currency(player.session)
        return player.endowment_euro_1
        return player.endowment_euro_2


def part_fee(player: Player):
    player.part_fee = player.session.config['participation_fee']
    return player.part_fee


def auszahlung_euro(player: Player):
    if func_sequence(player.subsession) == 1:
        player.auszahlung_euro_1 = player.session.config[
            'participation_fee'
        ] + player.endowment.to_real_world_currency(player.session)
        return player.auszahlung_euro_1
    else:
        player.auszahlung_euro_1 = player.session.config[
            'participation_fee'
        ] + player.payoff_1.to_real_world_currency(player.session)
        player.auszahlung_euro_2 = player.session.config[
            'participation_fee'
        ] + player.endowment.to_real_world_currency(player.session)
        return player.auszahlung_euro_1
        return player.auszahlung_euro_2

def check_wrong_anwers(player: Player):
    if player.rand == 1:
        if player.wrong_answer1 + player.wrong_answer2 + player.wrong_answer3 + player.wrong_answer4 + player.wrong_answer5 + player.wrong_answer6 >= 100:
            return False
        else:
            return True
    else:
        if player.wrong_answer1 + player.wrong_answer2 + player.wrong_answer3 + player.wrong_answer4 + player.wrong_answer5_2 + player.wrong_answer6 >= 100:
            return False
        else:
            return True


# PAGES
# translations
def trans_question_incorrectly(number):
    return ('Frage {} wurde falsch beantwortet.').format(number)


class Instruction_Page(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        if player.rand == 1:
            return [
                'comprehension_question2',
                'comprehension_question3',
                'comprehension_question4',
                'comprehension_question5',
                'comprehension_question6',
            ]
        else:
            return [
                'comprehension_question2',
                'comprehension_question3',
                'comprehension_question4',
                'comprehension_question5_2',
                'comprehension_question6',
            ]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            sequence=func_sequence(player.subsession), periode=func_period(player.subsession)
        )
        # context =  vars_for_template(self.player)
        # context.update(
        #    image_path12_LifeCycle = ('graphics/12_periods/LifeCycle.png').format(self.round_number),
        #    image_path12_income= ('graphics/12_periods/LifeCycleIncome.png').format(self.round_number),
        #    image_path12_rest= ('graphics/12_periods/LifeCycle_RestPhase.png').format(self.round_number),
        #    image_path12_questionnaire= ('graphics/12_periods/LifeCycle_Questionnaire.png').format(self.round_number),
        #    image_path12_payoff= ('graphics/12_periods/LifeCycle_Payoff.png').format(self.round_number),
        #    image_path12_test= ('graphics/12_periods/LifeCycle_ComprehensionTest.png').format(self.round_number),
        # )
        # return context

    # def comprehension_question1_error_message(self, value):
    #    if value != 2:
    #        self.player.wrong_answer1 += 1
    #        return trans_question_incorrectly(1)
    @staticmethod
    def comprehension_question2_error_message(player: Player, value):
        if value != 0:
            player.wrong_answer2 += 1
            return trans_question_incorrectly(1)

    @staticmethod
    def comprehension_question3_error_message(player: Player, value):
        if value != 0:
            player.wrong_answer3 += 1
            return trans_question_incorrectly(2)

    @staticmethod
    def comprehension_question4_error_message(player: Player, value):
        if value != 1:
            player.wrong_answer4 += 1
            return trans_question_incorrectly(3)

    @staticmethod
    def comprehension_question5_error_message(player: Player, value):
        if value != 1:
            player.wrong_answer5 += 1
            return trans_question_incorrectly(4)

    @staticmethod
    def comprehension_question5_2_error_message(player: Player, value):
        if value != 2:
            player.wrong_answer5_2 += 1
            return trans_question_incorrectly(4)

    @staticmethod
    def comprehension_question6_error_message(player: Player, value):
        if value != 2:
            player.wrong_answer6 += 1
            return trans_question_incorrectly(5)


class comprehension_check(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    def vars_for_template(player: Player):
        context =  player.vars_for_template()
        context.update(
            comprehension_check= check_wrong_anwers(),
            wrong_answers= player.wrong_answer1 + player.wrong_answer2 + player.wrong_answer3 + player.wrong_answer4 + player.wrong_answer5 + player.wrong_answer6,
        )
        return context


#######################################################################################################
class New_Sequence(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.sequence_length + 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            sequence=func_sequence(player.subsession), periode=func_period(player.subsession)
        )


class Wait_Page(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            if group.round_number != 1:
                access_data(player)
                access_seq_data(player)
            if group.round_number == Constants.sequence_length + 1:
                player.endowment = 1500
                player.anzahlA = 5
                player.anzahlB = 5


class MyPage2(Page):
    form_model = 'player'
    form_fields = ['verkaufA', 'kaufA', 'verkaufB', 'kaufB']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.round_number <= 3:
            second = 120
        else:
            second = 60
        return second

    @staticmethod
    def after_all_players_arrive(player: Player):
        if func_period(player.subsession) >= 2:
            marktpreisA_alt(player.group)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            marktpreisA_alt=marktpreisA_alt(player.group),
            marktpreisB_alt=marktpreisB_alt(player.group),
            sequence=func_sequence(player.subsession),
            periode=func_period(player.subsession),
        )

    @staticmethod
    def error_message(player: Player, values):
        # print('values is', values)
        if values['kaufA'] is None:
            pass
        else:
            if values['kaufA'] > player.endowment:
                return 'Ihre Nachfrage darf Ihr verfügbares Bankguthaben nicht übersteigen!'
            else:
                pass
        if values['kaufB'] is None:
            pass
        else:
            if values['kaufB'] > player.endowment:
                return 'Ihre Nachfrage darf Ihr verfügbares Bankguthaben nicht übersteigen!'
            else:
                pass
        if values['kaufA'] is None or values['kaufB'] is None:
            pass
        else:
            if values['kaufA'] + values['kaufB'] > player.endowment:
                return 'Die Summe der Nachfragen der Aktien beider Unternehmen darf Ihr verfügbares Bankguthaben nicht übersteigen!'
        if values['verkaufA'] is None:
            pass
        else:
            if values['verkaufA'] > 0 and player.anzahlA == 0:
                if player.rand == 1:
                    return 'Sie können keine A Aktie verkaufen, da Sie keine A Aktie im Portfolio haben.'
                else:
                    return 'Sie können keine B Aktie verkaufen, da Sie keine B Aktie im Portfolio haben.'
        if values['kaufA'] is None or values['verkaufA'] is None:
            pass
        else:
            if values['verkaufA'] <= values['kaufA']:
                return 'Ihre Nachfrage (= Kauf) kann nicht über oder gleich dem Angebot (= Verkauf) liegen. Sie würden mit sich selber handeln.'
        if values['verkaufB'] is None:
            pass
        else:
            if values['verkaufB'] > 0 and player.anzahlB == 0:
                if player.rand == 1:
                    return 'Sie können keine B Aktie verkaufen, da Sie keine B Aktie im Portfolio haben.'
                else:
                    return 'Sie können keine A Aktie verkaufen, da Sie keine A Aktie im Portfolio haben.'
        if values['kaufB'] is None or values['verkaufB'] is None:
            pass
        else:
            if values['verkaufB'] <= values['kaufB']:
                return 'Ihre Nachfrage (= Kauf) kann nicht über oder gleich dem Angebot (= Verkauf) liegen. Sie würden mit sich selber handeln.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_value_verkaufA(player)
        set_value_verkaufB(player)
        set_value_kaufA(player)
        set_value_kaufB(player)


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        verkaufA_liste(group)
        verkaufB_liste(group)
        kaufA_liste(group)
        kaufB_liste(group)
        datenA_verkauf(group)
        datenA_kauf(group)
        rank_verkaufA(group)
        rank_kaufA(group)
        datenA_verkauf_liste(group)
        datenA_kauf_liste(group)
        datenB_verkauf(group)
        datenB_kauf(group)
        rank_verkaufB(group)
        rank_kaufB(group)
        datenB_verkauf_liste(group)
        datenB_kauf_liste(group)
        rankA(group)
        rankB(group)
        marktpreisA_rech(group)
        marktpreisB_rech(group)
        handelA(group)
        handelB(group)
        ausfuhrung(group)
        dividende_rech(group)


class Results2(Page):
    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.round_number <= 3:
            second = 120
        else:
            second = 60
        return second

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'verkaufA_liste': player.group.verkaufA_liste,
            'kaufA_liste': player.group.kaufA_liste,
            'marktpreisA': player.group.marktpreisA,
            'anzahlA': player.anzahlA,
            'endowment': player.endowment,
            'endowmentalt': player.endowmentalt,
            'divA': player.group.dividendeA,
            'gesdiviA': player.gesdiviA,
            'datenA_verkauf_liste': player.group.datenA_verkauf_liste,
            'verkaufB_liste': player.group.verkaufB_liste,
            'kaufB_liste': player.group.kaufB_liste,
            'marktpreisB': player.group.marktpreisB,
            'anzahlB': player.anzahlB,
            'divB': player.group.dividendeB,
            'gesdiviB': player.gesdiviB,
            'datenB_verkauf_liste': player.group.datenB_verkauf_liste,
            'dividende_rech': player.group.dividende_rech,
            'dividendeA': player.group.dividendeA,
            'dividendeB': player.group.dividendeB,
            'sequence': func_sequence(player.subsession),
            'periode': func_period(player.subsession),
        }


class ResultsWaitPage2(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    @staticmethod
    def is_displayed(player: Player):
        return func_period(player.subsession) == Constants.sequence_length


class Ende(Page):
    @staticmethod
    def is_displayed(player: Player):
        return func_period(player.subsession) == Constants.sequence_length

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'anzahlA': player.anzahlA,
            'anzahlB': player.anzahlB,
            'endowment': player.endowment,
            'endowment_euro': player.endowment_euro,
            'endowment_ende': player.endowment_ende,
            'auszahlung_euro': player.auszahlung_euro,
            'part_fee': player.part_fee,
            'auszahlung': player.participant.payoff_plus_participation_fee(),
            'sequence': func_sequence(player.subsession),
            'periode': func_period(player.subsession),
        }


class Uebersicht(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'sequence': func_sequence(player.subsession),
            'periode': func_period(player.subsession),
        }


page_sequence = [
    Instruction_Page,
    comprehension_check,
    New_Sequence,
    Wait_Page,
    MyPage2,
    ResultsWaitPage,
    Results2,
    ResultsWaitPage2,
    Ende,
    Uebersicht,
]
