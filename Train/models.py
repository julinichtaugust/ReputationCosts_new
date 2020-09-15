import itertools


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

import random


author = 'Your name here'

doc = """
Your app description 4
"""


class Constants(BaseConstants):
    name_in_url = 'Train'
    players_per_group = 6
    num_rounds = 2

    #try_endowmwnt = 100
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
    #try_player = [1, 2, 3, 4, 5, 6]

    seat_number = models.IntegerField(
        min=0,
        max=18,
        label=("Bitte geben Sie Ihre Sitzplatznummer ein"),
        blank=False,
    )


    train_question1 = models.IntegerField(
        verbose_name=(
            "Frage 1: In welches Phase können Sie Aktien kaufen und verkaufen?"),
        initial=1,
        choices=[
            [0, ('Dividendenphase')],
            [1, ('Handelsphase')]],
        widget=widgets.RadioSelect,
    )

    #comprehension_question1 = models.IntegerField(
    #    verbose_name=(
    #        "Frage 1: Welche der folgenden Aussagen bezüglich der Vergütung am Ende des Experiments ist richtig?"),
    #    initial = 2,
    #    choices=[[0, ('Das durchschnittliche Endvermögen der beiden Sequenzen wird am Ende des Experiments ausgezahlt.')],
    #             [1, ('Die Summe des gesamten Vermögens beider Sequenzen wird am Ende des Experiments ausgezahlt.')],
    #             [2, ('Nur das Endvermögen einer der zwei Sequenzen wird am Ende des Experiments vergütet.')]],
    #    widget=widgets.RadioSelect,
    #)

    # Frage zu Anzahl Perioden
    # Frage zu Unsicherheit Dividenden

    train_wrong_answer1 = models.IntegerField(initial=0)


# Kauf- und Verkaufspreis auf 0 setzen, falls Eingabe == None

    def set_value_try_verkauf(self):
        if self.try_verkauf == None:
            self.try_verkauf = 99999

    def set_value_try_kauf(self):
        if self.try_kauf == None:
            self.try_kauf = 0

# Für Proberunde

    def try_verkauf_liste(self):
        if self.round_number == 1:
            self.try_verkauf_liste = [
                {
                    'SPIELER': 1,
                    'ANGEBOT': self.try_verkauf
                },
                {
                    'SPIELER': 2,
                    'ANGEBOT': c(6)
                },
                {
                    'SPIELER': 3,
                    'ANGEBOT': c(4)
                },
                {
                    'SPIELER': 4,
                    'ANGEBOT': c(9)
                },
                {
                    'SPIELER': 5,
                    'ANGEBOT': c(5)
                },
                {
                    'SPIELER': 6,
                    'ANGEBOT': c(3)
                }
            ]
            #print(self.try_verkauf_liste)
        else:
            self.try_verkauf_liste = [
                {
                    'SPIELER': 1,
                    'ANGEBOT': self.try_verkauf
                },
                {
                    'SPIELER': 2,
                    'ANGEBOT': c(3)
                },
                {
                    'SPIELER': 3,
                    'ANGEBOT': c(4)
                },
                {
                    'SPIELER': 4,
                    'ANGEBOT': c(5)
                },
                {
                    'SPIELER': 5,
                    'ANGEBOT': c(2.5)
                },
                {
                    'SPIELER': 6,
                    'ANGEBOT': c(2)
                }
            ]
        return self.try_verkauf_liste


    def try_daten_verkauf(self):
        v = self.try_verkauf_liste
        w1=0
        self.try_daten_verkauf = sorted(v, key=lambda k: (k['ANGEBOT'],random.random()))
        for item in self.try_daten_verkauf:
            w1 = w1+1
            item.update({'RANK': w1})
        #print(self.try_daten_verkauf)
        return self.try_daten_verkauf

    def try_kauf_liste(self):
        if self.round_number == 1:
            self.try_kauf_liste = [
                {
                    'SPIELER': 1,
                    'NACHFRAGE': self.try_kauf
                },
                {
                    'SPIELER': 2,
                    'NACHFRAGE': c(6)
                },
                {
                    'SPIELER': 3,
                    'NACHFRAGE': c(5)
                },
                {
                    'SPIELER': 4,
                    'NACHFRAGE': c(8)
                },
                {
                    'SPIELER': 5,
                    'NACHFRAGE': c(4)
                },
                {
                    'SPIELER': 6,
                    'NACHFRAGE': c(3)
                }
            ]
        else:
            self.try_kauf_liste = [
                {
                    'SPIELER': 1,
                    'NACHFRAGE': self.try_kauf
                },
                {
                    'SPIELER': 2,
                    'NACHFRAGE': c(3)
                },
                {
                    'SPIELER': 3,
                    'NACHFRAGE': c(2.5)
                },
                {
                    'SPIELER': 4,
                    'NACHFRAGE': c(4)
                },
                {
                    'SPIELER': 5,
                    'NACHFRAGE': c(2)
                },
                {
                    'SPIELER': 6,
                    'NACHFRAGE': c(1.5)
                }
            ]
        #print(self.try_kauf_liste)
        return self.try_kauf_liste

    def try_daten_kauf(self):
        q = self.try_kauf_liste
        w2=0
        self.try_daten_kauf = sorted(q, key=lambda k: (k['NACHFRAGE'],random.random()), reverse=True)
        for item in self.try_daten_kauf:
            w2 = w2+1
            item.update({'RANK': w2})
        #print(self.try_daten_kauf)
        return self.try_daten_kauf

    def try_verkauf_liste_h(self):
        if self.round_number == 1:
            self.try_verkauf_liste_h = [self.try_verkauf, 6, 4, 9, 5, 3]
        else:
            self.try_verkauf_liste_h = [self.try_verkauf, 3, 4, 5, 2.5, 2]
        self.try_verkauf_liste_h.sort()
        print(self.try_verkauf_liste_h)
        return self.try_verkauf_liste_h

    def try_kauf_liste_h(self):
        if self.round_number == 1:
            self.try_kauf_liste_h = [self.try_kauf, 6, 5, 8, 4, 3]
        else:
            self.try_kauf_liste_h = [self.try_kauf, 3, 2.5, 4, 2, 1.5]
        self.try_kauf_liste_h.sort(reverse=True)
        print(self.try_kauf_liste_h)
        return self.try_kauf_liste_h

    def try_rank(self):
        self.try_clearing_rank = 0
        for i in range(1,Constants.players_per_group+1,1):
            a = i-1
            if self.try_kauf_liste_h[a] >= self.try_verkauf_liste_h[a]:
                self.try_clearing_rank = i
            else:
                pass
        print(self.try_clearing_rank)

    def try_rank_verkauf_player(self):
        self.try_rank_verkauf_player = (next((i for i, item in enumerate(self.try_daten_verkauf) if item["SPIELER"] == 1), None))+1
        #print(self.try_daten_verkauf)
        #print(self.try_rank_verkauf_player)
        return self.try_rank_verkauf_player

    def try_rank_kauf_player(self):
        self.try_rank_kauf_player = (next((i for i, item in enumerate(self.try_daten_kauf) if item["SPIELER"] == 1), None))+1
        #print(self.try_daten_kauf)
        #print(self.try_rank_kauf_player)
        return self.try_rank_kauf_player

    def try_marktpreis_rech(self):
        for i in range(Constants.players_per_group, 0, -1):
            a = i-1
            if self.try_clearing_rank == i:
                self.try_marktpreis = ((self.try_kauf_liste_h[a] + self.try_verkauf_liste_h[a])/2)
                #print(self.try_clearing_rank)
                #print(self.try_kauf_liste)
                #print(self.try_kauf_liste_h)
                #print(self.try_marktpreis)
            else:
                pass


    def try_handel(self):
        if self.try_rank_kauf_player <= self.try_clearing_rank:
            self.try_is_trade_kauf = True
        else:
            pass
        if self.try_rank_verkauf_player <= self.try_clearing_rank:
            self.try_is_trade_verkauf = True
        else:
            pass

    def try_ausfuhrung(self):
            if self.try_is_trade_kauf == True and self.try_is_trade_verkauf == True:
                pass
            else:
                if self.try_is_trade_kauf == True and self.try_is_trade_verkauf == False:
                    self.try_anzahl = self.try_anzahl + 1
                    self.try_endowment = self.try_endowment - self.try_marktpreis
                else:
                    if self.try_is_trade_verkauf == True and self.try_is_trade_kauf == False:
                        self.try_anzahl = self.try_anzahl -1
                        self.try_endowment = self.try_endowment + self.try_marktpreis
                    else:
                        pass




    def try_dividende(self):
        self.try_dividende = c(random.choice(Constants.try_divi))
        self.try_gesdivi = self.try_anzahl * self.try_dividende
        return self.try_dividende

    def try_vermogen(self):
        self.try_endowment = self.try_endowment + self.try_gesdivi
        return self.try_endowment

    def access_data(self):
        self.try_endowment = self.in_round(self.round_number - 1).try_endowment
        self.try_anzahl = self.in_round(self.round_number - 1).try_anzahl




