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

import operator


author = 'Your name here'

doc = """
Your app description 4
"""


class Constants(BaseConstants):
    name_in_url = 'RepCostExperiment'
    players_per_group = 3
    num_rounds = 1

    endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    verkaufA_1 = models.CurrencyField()
    verkaufA_2 = models.CurrencyField()
    verkaufA_3 = models.CurrencyField()
    kaufA_1 = models.CurrencyField()
    kaufA_2 = models.CurrencyField()
    kaufA_3 = models.CurrencyField()
    marktpreisA = models.CurrencyField()
    clearing_rankA = models.IntegerField()



    def verkaufA_liste(self):
        players = self.get_players()
        self.verkaufA_liste = [p.verkaufA for p in players]
        self.verkaufA_liste.sort(reverse=True)
        self.verkaufA_1 = self.verkaufA_liste[-1]
        self.verkaufA_2 = self.verkaufA_liste[-2]
        self.verkaufA_3 = self.verkaufA_liste[-3]

    def kaufA_liste(self):
        players = self.get_players()
        self.kaufA_liste = [p.kaufA for p in players]
        self.kaufA_liste.sort()
        self.kaufA_1 = self.kaufA_liste[-1]
        self.kaufA_2 = self.kaufA_liste[-2]
        self.kaufA_3 = self.kaufA_liste[-3]


    def marktpreisA_rech(self):
       if self.kaufA_3 >= self.verkaufA_3:
           self.marktpreisA = (self.kaufA_liste[-3]+self.verkaufA_liste[-3])/2
       else:
           if self.kaufA_2 >= self.verkaufA_2:
               self.marktpreisA = (self.kaufA_liste[-2]+self.verkaufA_liste[-2])/2
           else:
               if self.kaufA_1 >= self.verkaufA_1:
                   self.marktpreisA = (self.kaufA_liste[-1] + self.verkaufA_liste[-1])/2
               else:
                   pass

    def handelA(self):
        players = self.get_players()
        for p in players:
            if p.kaufA >= self.marktpreisA:
                p.is_trade_kaufA = True
            else:
                pass
            if p.verkaufA <= self.marktpreisA:
                p.is_trade_verkaufA = True
            else:
                pass

    def ausführung(self):
        players = self.get_players()
        for p in players:
            if p.is_trade_kaufA == True and p.is_trade_verkaufA == True:
                pass
            else:
                if p.is_trade_kaufA == True:
                    p.anzahlA = p.anzahlA + 1
                    p.endowment = p.endowment - self.marktpreisA
                else:
                    if p.is_trade_verkaufA == True:
                        p.anzahlA = p.anzahlA -1
                        p.endowment = p.endowment + self.marktpreisA
                    else:
                        pass

    def daten(self):
        players = self.get_players()
        v = []
        k = []
        for p in players:
            v.append({'SPIELER': p.id_in_group, 'ANGEBOT': p.verkaufA})
        liste_verkaufA = sorted(v, key=lambda k: k['ANGEBOT'])
        print(liste_verkaufA)
        for p in players:
            k.append({'SPIELER': p.id_in_group, 'NACHFRAGE': p.kaufA})
        liste_kaufA = sorted(k, key=lambda k: k['NACHFRAGE'], reverse=True)
        print(liste_kaufA)




class Player(BasePlayer):
    verkaufA = models.CurrencyField(label='Angebot A:')
    kaufA = models.CurrencyField(label='Nachfrage A:')
    endowment = models.CurrencyField(initial=1000)
    is_trade_kaufA = models.BooleanField(initial=False)
    is_trade_verkaufA = models.BooleanField(initial=False)
    anzahlA = models.IntegerField(initial=5)
    rank_kaufA = models.IntegerField()
    rank_verkaufA = models.IntegerField()

