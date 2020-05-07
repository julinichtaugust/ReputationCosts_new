
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
    name_in_url = 'RepCostExperiment'
    players_per_group = 3
    num_rounds = 2

    endowment = 100
    diviA = [0, 5, 15, 20]
    diviB = [0, 5, 15, 20]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    marktpreisA = models.CurrencyField()
    clearing_rankA = models.IntegerField()
    dividendeA = models.CurrencyField()
    marktpreisB = models.CurrencyField()
    clearing_rankB = models.IntegerField()
    dividendeB = models.CurrencyField()



# Sortierte Liste der Verkaufspreise (Angebote: von klein nach groß)
    def verkaufA_liste(self):
        players = self.get_players()
        self.verkaufA_liste = [p.verkaufA for p in players]
        self.verkaufA_liste.sort()
        return self.verkaufA_liste

    def verkaufB_liste(self):
        players = self.get_players()
        self.verkaufB_liste = [p.verkaufB for p in players]
        self.verkaufB_liste.sort()
        return self.verkaufB_liste

# Sortierte Liste der Kaufspreise (Nachfragen: von groß nach klein)
    def kaufA_liste(self):
        players = self.get_players()
        self.kaufA_liste = [p.kaufA for p in players]
        self.kaufA_liste.sort(reverse=True)
        return self.kaufA_liste

    def kaufB_liste(self):
        players = self.get_players()
        self.kaufB_liste = [p.kaufB for p in players]
        self.kaufB_liste.sort(reverse=True)
        return self.kaufB_liste
################################################################################################
    def datenA_verkauf(self):
        players = self.get_players()
        v = []
        w1=0
        for p in players:
            v.append({'SPIELER': p.id_in_group, 'ANGEBOT': p.verkaufA})
            self.datenA_verkauf = sorted(v, key=lambda k: (k['ANGEBOT'],random.random()))
        for item in self.datenA_verkauf:
            w1 = w1+1
            item.update({'RANK': w1})
        return self.datenA_verkauf

    def datenA_kauf(self):
        players = self.get_players()
        k = []
        w2=0
        for p in players:
            k.append({'SPIELER': p.id_in_group, 'NACHFRAGE': p.kaufA})
            self.datenA_kauf = sorted(k, key=lambda k: (k['NACHFRAGE'],random.random()), reverse=True)
        for item in self.datenA_kauf:
            w2 = w2+1
            item.update({'RANK': w2})
        return self.datenA_kauf

    def rank_verkaufA(self):
        players = self.get_players()
        datenA_verkauf = self.datenA_verkauf
        print(datenA_verkauf)
        for p in players:
            for item in datenA_verkauf:
                if p.id_in_group == item['SPIELER']:
                    p.rank_verkaufA = item['RANK']
                else:
                    pass

    def rank_kaufA(self):
        players = self.get_players()
        datenA_kauf = self.datenA_kauf
        for p in players:
            for item in datenA_kauf:
                if p.id_in_group == item['SPIELER']:
                    p.rank_kaufA = item['RANK']
                else:
                    pass

    def datenA_verkauf_liste(self):
        self.datenA_verkauf_liste = [d['SPIELER'] for d in self.datenA_verkauf]


    def datenA_kauf_liste(self):
        self.datenA_kauf_liste = [d['SPIELER'] for d in self.datenA_kauf]

#############################################################

    def datenB_verkauf(self):
        players = self.get_players()
        c = []
        w3 = 0
        for p in players:
            c.append({'SPIELER': p.id_in_group, 'ANGEBOT': p.verkaufB})
            self.datenB_verkauf = sorted(c, key=lambda k: (k['ANGEBOT'], random.random()))
        for item in self.datenB_verkauf:
            w3 = w3 + 1
            item.update({'RANK': w3})
        return self.datenB_verkauf

    def datenB_kauf(self):
        players = self.get_players()
        h = []
        w4 = 0
        for p in players:
            h.append({'SPIELER': p.id_in_group, 'NACHFRAGE': p.kaufB})
            self.datenB_kauf = sorted(h, key=lambda k: (k['NACHFRAGE'], random.random()), reverse=True)
        for item in self.datenB_kauf:
            w4 = w4 + 1
            item.update({'RANK': w4})
        print(self.datenB_kauf)
        return self.datenB_kauf

    def rank_verkaufB(self):
        players = self.get_players()
        datenB_verkauf = self.datenB_verkauf
        print(datenB_verkauf)
        for p in players:
            for item in datenB_verkauf:
                if p.id_in_group == item['SPIELER']:
                    p.rank_verkaufB = item['RANK']
                else:
                    pass

    def rank_kaufB(self):
        players = self.get_players()
        datenB_kauf = self.datenB_kauf
        for p in players:
            for item in datenB_kauf:
                if p.id_in_group == item['SPIELER']:
                    p.rank_kaufB = item['RANK']
                else:
                    pass

    def datenB_verkauf_liste(self):
        self.datenB_verkauf_liste = [d['SPIELER'] for d in self.datenB_verkauf]

    def datenB_kauf_liste(self):
        self.datenB_kauf_liste = [d['SPIELER'] for d in self.datenB_kauf]

###########################################

# Rank bestimmen zu dem Markt geräumt wird (Nachrage >= Angebot)
    def rankA(self):
        self.clearing_rankA = 0
        for i in range(1,Constants.players_per_group+1,1):
            a = i-1
            if self.kaufA_liste[a] >= self.verkaufA_liste[a]:
                self.clearing_rankA = i
            else:
                pass

    def rankB(self):
        self.clearing_rankB = 0
        for i in range(1,Constants.players_per_group+1,1):
            a = i-1
            if self.kaufB_liste[a] >= self.verkaufB_liste[a]:
                self.clearing_rankB = i
            else:
                pass

# Marktpreis in Abhänigkeit des bestimmten Ranks berechnen - Mittelwert aus Nachfrage und Angebot
    def marktpreisA_rech(self):
        for i in range(Constants.players_per_group, 0, -1):
            a = i-1
            if self.clearing_rankA == i:
                self.marktpreisA = ((self.kaufA_liste[a] + self.verkaufA_liste[a])/2)
            else:
                pass


    def marktpreisB_rech(self):
        for i in range(Constants.players_per_group, 0, -1):
            a = i-1
            if self.clearing_rankB == i:
                self.marktpreisB = ((self.kaufB_liste[a] + self.verkaufB_liste[a])/2)
            else:
                pass

# Jedem Spieler zuweisen, ob er ein Aktie verkauft hat oder kauft (Abfrage ob eigener Rang über "clearing" Rank
    def handelA(self):
        players = self.get_players()
        for p in players:
            if p.rank_kaufA <= self.clearing_rankA:
              p.is_trade_kaufA = True
            else:
                pass
            if p.rank_verkaufA <= self.clearing_rankA:
              p.is_trade_verkaufA = True
            else:
                pass

    def handelB(self):
        players = self.get_players()
        for p in players:
            if p.rank_kaufB <= self.clearing_rankB:
              p.is_trade_kaufB = True
            else:
                pass
            if p.rank_verkaufB <= self.clearing_rankB:
              p.is_trade_verkaufB = True
            else:
                pass

# Ausführen des Handels, in dem jedem Spieler Aktien zugerechnet und abgezogen werden, sowie die Ausstattung angepasst wird
    def ausfuhrung(self):
        players = self.get_players()
        for p in players:
            p.endowmentalt = p.endowment
            if p.is_trade_kaufA == True and p.is_trade_verkaufA == True:
                pass
            else:
                if p.is_trade_kaufA == True and p.is_trade_verkaufA == False:
                    p.anzahlA = p.anzahlA + 1
                    p.endowment = p.endowment - self.marktpreisA
                else:
                    if p.is_trade_verkaufA == True and p.is_trade_kaufA == False:
                        p.anzahlA = p.anzahlA -1
                        p.endowment = p.endowment + self.marktpreisA
                    else:
                        pass

            if p.is_trade_kaufB == True and p.is_trade_verkaufB == True:
                pass
            else:
                if p.is_trade_kaufB == True and p.is_trade_verkaufB == False:
                    p.anzahlB = p.anzahlB + 1
                    p.endowment = p.endowment - self.marktpreisB
                else:
                    if p.is_trade_verkaufB == True and p.is_trade_kaufB == False:
                        p.anzahlB = p.anzahlB -1
                        p.endowment = p.endowment + self.marktpreisB
                    else:
                        pass

# Nach Abschluss des Handels, Auszahlung der Dividende pro Aktie im neuen Portfolio
    def dividende_rech(self):
        self.dividendeA = c(random.choice(Constants.diviA))
        self.dividendeB = c(random.choice(Constants.diviB))
        players = self.get_players()
        for p in players:
            p.endowment = p.endowment + p.anzahlA * self.dividendeA + p.anzahlB * self.dividendeB
            p.gesdiviA = p.anzahlA * self.dividendeA
            p.gesdiviB = p.anzahlB * self.dividendeB

class Player(BasePlayer):
    verkaufA = models.CurrencyField(label='Angebot A:')
    kaufA = models.CurrencyField(label='Nachfrage A:')
    endowment = models.CurrencyField(initial=1000)
    endowmentalt = models.CurrencyField()
    is_trade_kaufA = models.BooleanField(initial=False)
    is_trade_verkaufA = models.BooleanField(initial=False)
    anzahlA = models.IntegerField(initial=5)
    rank_verkaufA = models.IntegerField()
    rank_kaufA = models.IntegerField()
    gesdiviA = models.CurrencyField()

    verkaufB = models.CurrencyField(label='Angebot B:')
    kaufB = models.CurrencyField(label='Nachfrage B:')
    is_trade_kaufB = models.BooleanField(initial=False)
    is_trade_verkaufB = models.BooleanField(initial=False)
    anzahlB = models.IntegerField(initial=5)
    rank_verkaufB = models.IntegerField()
    rank_kaufB = models.IntegerField()
    gesdiviB = models.CurrencyField()

# Werte der Vorperiode holen
    def access_data(self):
        self.endowment = self.in_round(self.round_number - 1).endowment
        self.anzahlA = self.in_round(self.round_number - 1).anzahlA
        self.anzahlB = self.in_round(self.round_number - 1).anzahlB



