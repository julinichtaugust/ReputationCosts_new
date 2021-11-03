import itertools
import random

from otree.api import *


author = 'Your name here'
doc = """
Your app description 4
"""


class Constants(BaseConstants):
    name_in_url = 'Train'
    players_per_group = 6
    num_rounds = 2
    # try_endowmwnt = 100
    try_divi = [1, 2, 3, 4, 5]
    try_player = [1, 2, 3, 4, 5, 6]
    fix = 3.00


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    try_verkauf = models.CurrencyField(blank=True)
    try_kauf = models.CurrencyField(blank=True)
    try_endowment = models.CurrencyField(initial=100)
    try_anzahl = models.IntegerField(initial=2)
    try_gesdivi = models.CurrencyField()
    try_marktpreis = models.CurrencyField()
    try_dividende = models.CurrencyField()
    try_clearing_rank = models.IntegerField()
    try_is_trade_kauf = models.BooleanField(initial=False)
    try_is_trade_verkauf = models.BooleanField(initial=False)
    # try_player = [1, 2, 3, 4, 5, 6]
    seat_number = models.IntegerField(
        min=0,
        max=18,
        label=("Bitte geben Sie Ihre Sitzplatznummer ein"),
        blank=False,
    )
    train_question1 = models.IntegerField(
        verbose_name=("Frage 1: In welches Phase können Sie Aktien kaufen und verkaufen?"),
        initial=1,
        choices=[[0, ('Dividendenphase')], [1, ('Handelsphase')]],
        widget=widgets.RadioSelect,
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
    # Frage zu Anzahl Perioden
    # Frage zu Unsicherheit Dividenden
    train_wrong_answer1 = models.IntegerField(initial=0)


# Kauf- und Verkaufspreis auf 0 setzen, falls Eingabe == None
# FUNCTIONS
def set_value_try_verkauf(player: Player):
    if player.try_verkauf == None:
        player.try_verkauf = 99999


def set_value_try_kauf(player: Player):
    if player.try_kauf == None:
        player.try_kauf = 0


# Für Proberunde
def try_verkauf_liste(player: Player):
    if player.round_number == 1:
        player.try_verkauf_liste = [
            {'SPIELER': 1, 'ANGEBOT': player.try_verkauf},
            {'SPIELER': 2, 'ANGEBOT': c(6)},
            {'SPIELER': 3, 'ANGEBOT': c(4)},
            {'SPIELER': 4, 'ANGEBOT': c(9)},
            {'SPIELER': 5, 'ANGEBOT': c(5)},
            {'SPIELER': 6, 'ANGEBOT': c(3)},
        ]
        # print(self.try_verkauf_liste)
    else:
        player.try_verkauf_liste = [
            {'SPIELER': 1, 'ANGEBOT': player.try_verkauf},
            {'SPIELER': 2, 'ANGEBOT': c(3)},
            {'SPIELER': 3, 'ANGEBOT': c(4)},
            {'SPIELER': 4, 'ANGEBOT': c(5)},
            {'SPIELER': 5, 'ANGEBOT': c(2.5)},
            {'SPIELER': 6, 'ANGEBOT': c(2)},
        ]
    return player.try_verkauf_liste


def try_daten_verkauf(player: Player):
    v = player.try_verkauf_liste
    w1 = 0
    player.try_daten_verkauf = sorted(v, key=lambda k: (k['ANGEBOT'], random.random()))
    for item in player.try_daten_verkauf:
        w1 = w1 + 1
        item.update({'RANK': w1})
    # print(self.try_daten_verkauf)
    return player.try_daten_verkauf


def try_kauf_liste(player: Player):
    if player.round_number == 1:
        player.try_kauf_liste = [
            {'SPIELER': 1, 'NACHFRAGE': player.try_kauf},
            {'SPIELER': 2, 'NACHFRAGE': c(6)},
            {'SPIELER': 3, 'NACHFRAGE': c(5)},
            {'SPIELER': 4, 'NACHFRAGE': c(8)},
            {'SPIELER': 5, 'NACHFRAGE': c(4)},
            {'SPIELER': 6, 'NACHFRAGE': c(3)},
        ]
    else:
        player.try_kauf_liste = [
            {'SPIELER': 1, 'NACHFRAGE': player.try_kauf},
            {'SPIELER': 2, 'NACHFRAGE': c(3)},
            {'SPIELER': 3, 'NACHFRAGE': c(2.5)},
            {'SPIELER': 4, 'NACHFRAGE': c(4)},
            {'SPIELER': 5, 'NACHFRAGE': c(2)},
            {'SPIELER': 6, 'NACHFRAGE': c(1.5)},
        ]
    # print(self.try_kauf_liste)
    return player.try_kauf_liste


def try_daten_kauf(player: Player):
    q = player.try_kauf_liste
    w2 = 0
    player.try_daten_kauf = sorted(q, key=lambda k: (k['NACHFRAGE'], random.random()), reverse=True)
    for item in player.try_daten_kauf:
        w2 = w2 + 1
        item.update({'RANK': w2})
    # print(self.try_daten_kauf)
    return player.try_daten_kauf


def try_verkauf_liste_h(player: Player):
    if player.round_number == 1:
        player.try_verkauf_liste_h = [player.try_verkauf, 6, 4, 9, 5, 3]
    else:
        player.try_verkauf_liste_h = [player.try_verkauf, 3, 4, 5, 2.5, 2]
    player.try_verkauf_liste_h.sort()
    # print(self.try_verkauf_liste_h)
    return player.try_verkauf_liste_h


def try_kauf_liste_h(player: Player):
    if player.round_number == 1:
        player.try_kauf_liste_h = [player.try_kauf, 6, 5, 8, 4, 3]
    else:
        player.try_kauf_liste_h = [player.try_kauf, 3, 2.5, 4, 2, 1.5]
    player.try_kauf_liste_h.sort(reverse=True)
    # print(self.try_kauf_liste_h)
    return player.try_kauf_liste_h


def try_rank(player: Player):
    player.try_clearing_rank = 0
    for i in range(1, Constants.players_per_group + 1, 1):
        a = i - 1
        if player.try_kauf_liste_h[a] >= player.try_verkauf_liste_h[a]:
            player.try_clearing_rank = i
        else:
            pass
    # print(self.try_clearing_rank)


def try_rank_verkauf_player(player: Player):
    player.try_rank_verkauf_player = (
        next((i for i, item in enumerate(player.try_daten_verkauf) if item["SPIELER"] == 1), None)
    ) + 1
    # print(self.try_daten_verkauf)
    # print(self.try_rank_verkauf_player)
    return player.try_rank_verkauf_player


def try_rank_kauf_player(player: Player):
    player.try_rank_kauf_player = (
        next((i for i, item in enumerate(player.try_daten_kauf) if item["SPIELER"] == 1), None)
    ) + 1
    # print(self.try_daten_kauf)
    # print(self.try_rank_kauf_player)
    return player.try_rank_kauf_player


def try_marktpreis_rech(player: Player):
    for i in range(Constants.players_per_group, 0, -1):
        a = i - 1
        if player.try_clearing_rank == i:
            player.try_marktpreis = (player.try_kauf_liste_h[a] + player.try_verkauf_liste_h[a]) / 2
            # print(self.try_clearing_rank)
            # print(self.try_kauf_liste)
            # print(self.try_kauf_liste_h)
            # print(self.try_marktpreis)
        else:
            pass


def try_handel(player: Player):
    if player.try_rank_kauf_player <= player.try_clearing_rank:
        player.try_is_trade_kauf = True
    else:
        pass
    if player.try_rank_verkauf_player <= player.try_clearing_rank:
        player.try_is_trade_verkauf = True
    else:
        pass


def try_ausfuhrung(player: Player):
    if player.try_is_trade_kauf == True and player.try_is_trade_verkauf == True:
        pass
    else:
        if player.try_is_trade_kauf == True and player.try_is_trade_verkauf == False:
            player.try_anzahl = player.try_anzahl + 1
            player.try_endowment = player.try_endowment - player.try_marktpreis
        else:
            if player.try_is_trade_verkauf == True and player.try_is_trade_kauf == False:
                player.try_anzahl = player.try_anzahl - 1
                player.try_endowment = player.try_endowment + player.try_marktpreis
            else:
                pass


def try_dividende(player: Player):
    player.try_dividende = c(random.choice(Constants.try_divi))
    player.try_gesdivi = player.try_anzahl * player.try_dividende
    return player.try_dividende


def try_vermogen(player: Player):
    player.try_endowment = player.try_endowment + player.try_gesdivi
    return player.try_endowment


def access_data(player: Player):
    player.try_endowment = player.in_round(player.round_number - 1).try_endowment
    player.try_anzahl = player.in_round(player.round_number - 1).try_anzahl


# PAGES
# translations
def trans_question_incorrectly(number):
    return ('Frage {} wurde falsch beantwortet.').format(number)


class Welcome(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class questions_pre(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return ['seat_number']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def risk_error_message(player: Player, value):
        if value == None:
            return "Diese Frage wurde nicht beantwortet."


class Instruction_Training(Page):
    form_model = 'player'
    # def get_form_fields(self):
    #   if self.player.rand == 1:
    #       return ['train_question1']
    #   else:
    #       return ['train_question1']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    # def train_question1_error_message(self, value):
    #    if value != 1:
    #        self.player.train_wrong_answer1 += 1
    #        return trans_question_incorrectly(1)


class Probe(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


#######################################################################################################
class Try1(Page):
    form_model = 'player'
    form_fields = ['try_verkauf', 'try_kauf']

    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1:
            return player.round_number == 1
        else:
            if player.round_number != 1:
                access_data(player)
                return player.round_number == 2

    @staticmethod
    def error_message(player: Player, values):
        if values['try_kauf'] is None:
            pass
        else:
            if values['try_kauf'] > player.try_endowment:
                return 'Die Nachfrage darf Ihr verfügbares Vermögen nicht übersteigen!'
        if values['try_kauf'] is None or values['try_verkauf'] is None:
            pass
        else:
            if values['try_verkauf'] <= values['try_kauf']:
                return 'Ihre Nachfrage kann nicht über oder gleich dem Angebot liegen. Sie würden mit sich selber handeln.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_value_try_verkauf(player)
        set_value_try_kauf(player)


class Try2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'try_verkauf_liste': player.try_verkauf_liste,
            'try_kauf_liste': player.try_kauf_liste,
            'try_marktpreis': player.try_marktpreis,
            'try_anzahl': player.try_anzahl,
            'try_endowment': player.try_endowment,
            'try_dividende': player.try_dividende,
            'try_daten_verkauf': player.try_daten_verkauf,
            'try_daten_kauf': player.try_daten_kauf,
            'try_verkauf_liste_h': player.try_verkauf_liste_h,
            'try_kauf_liste_h': player.try_kauf_liste_h,
            'try_rank': player.try_rank,
            'try_rank_verkauf_player': player.try_rank_verkauf_player,
            'try_rank_kauf_player': player.try_rank_kauf_player,
            'try_marktpreis_rech': player.try_marktpreis_rech,
            'try_handel': player.try_handel,
            'try_ausfuhrung': player.try_ausfuhrung,
            'try_vermogen': player.try_vermogen,
        }


class Train_Ende(Page):
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 2:
            return player.round_number == 2

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'try_verkauf_liste': player.try_verkauf_liste,
            'try_kauf_liste': player.try_kauf_liste,
            'try_marktpreis': player.try_marktpreis,
            'try_anzahl': player.try_anzahl,
            'try_endowment': player.try_endowment,
            'try_dividende': player.try_dividende,
            'try_daten_verkauf': player.try_daten_verkauf,
            'try_daten_kauf': player.try_daten_kauf,
            'try_verkauf_liste_h': player.try_verkauf_liste_h,
            'try_kauf_liste_h': player.try_kauf_liste_h,
            'try_rank': player.try_rank,
            'try_rank_verkauf_player': player.try_rank_verkauf_player,
            'try_rank_kauf_player': player.try_rank_kauf_player,
            'try_marktpreis_rech': player.try_marktpreis_rech,
            'try_handel': player.try_handel,
            'try_ausfuhrung': player.try_ausfuhrung,
            'try_vermogen': player.try_vermogen,
        }


########################################################################################################
page_sequence = [
    Welcome,
    questions_pre,
    Instruction_Training,
    Probe,
    Try1,
    Try2,
    Train_Ende,
]
