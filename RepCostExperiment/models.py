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
    diviA = [0,5,15,20]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    marktpreisA = models.CurrencyField()
    clearing_rankA = models.IntegerField()
    dividendeA = models.CurrencyField()

# Sortierte Liste der Verkaufspreise (Angebote: von klein nach groß)
    def verkaufA_liste(self):
        players = self.get_players()
        self.verkaufA_liste = [p.verkaufA for p in players]
        self.verkaufA_liste.sort()
        return self.verkaufA_liste

# Sortierte Liste der Kaufspreise (Nachfragen: von groß nach klein)
    def kaufA_liste(self):
        players = self.get_players()
        self.kaufA_liste = [p.kaufA for p in players]
        self.kaufA_liste.sort(reverse=True)
        return self.kaufA_liste

# Liste, in der pro Spieler ein Dict mit Spieler, Angebot/Nachfrage, Rank liegt, sortiert
    def daten(self):
        players = self.get_players()
        v = []
        k = []
        w1=0
        w2=0
        for p in players:
            v.append({'SPIELER': p.id_in_group, 'ANGEBOT': p.verkaufA})
        liste_verkaufA = sorted(v, key=lambda k: k['ANGEBOT'])
        for item in liste_verkaufA:
            w1 = w1+1
            item.update({'RANK': w1})

        for p in players:
            for item in liste_verkaufA:
                if p.id_in_group == item['SPIELER']:
                    p.rank_verkaufA = item['RANK']
                else:
                    pass

        for p in players:
            k.append({'SPIELER': p.id_in_group, 'NACHFRAGE': p.kaufA})
        liste_kaufA = sorted(k, key=lambda k: k['NACHFRAGE'], reverse=True)
        for item in liste_kaufA:
            w2 = w2+1
            item.update({'RANK': w2})

        for p in players:
            for item in liste_kaufA:
                if p.id_in_group == item['SPIELER']:
                    p.rank_kaufA = item['RANK']
                else:
                    pass

# Rank bestimmen zu dem Markt geräumt wird (Nachrage >= Angebot)
    def rank(self):
        print(self.verkaufA_liste)
        print(self.kaufA_liste)
        self.clearing_rankA = 0
        for i in range(1,Constants.players_per_group+1,1):
            a = i-1
            if self.kaufA_liste[a] >= self.verkaufA_liste[a]:
                self.clearing_rankA = i
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

# Ausführen des Handels, in dem jedem Spieler Aktien zugerechnet und abgezogen werden, sowie die Ausstattung angepasst wird
    def ausfuhrung(self):
        players = self.get_players()
        for p in players:
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

# Nach Abschluss des Handels, Auszahlung der Dividende pro Aktie im neuen Portfolio
    def dividende_rech(self):
        self.dividendeA = c(random.choice(Constants.diviA))
        players = self.get_players()
        for p in players:
            p.endowment = p.endowment + p.anzahlA * self.dividendeA


class Player(BasePlayer):
    verkaufA = models.CurrencyField(label='Angebot A:')
    kaufA = models.CurrencyField(label='Nachfrage A:')
    endowment = models.CurrencyField(initial=1000)
    is_trade_kaufA = models.BooleanField(initial=False)
    is_trade_verkaufA = models.BooleanField(initial=False)
    anzahlA = models.IntegerField(initial=5)
    rank_verkaufA = models.IntegerField()
    rank_kaufA = models.IntegerField()

# Werte der Vorperiode holen
    def access_data(self):
        self.endowment = self.in_round(self.round_number - 1).endowment
        self.anzahlA = self.in_round(self.round_number - 1).anzahlA




