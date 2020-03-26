from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Wait_Page(WaitPage):
    def after_all_players_arrive(self):
        for player in self.group.get_players():
            if self.round_number != 1:
                player.access_data()



class MyPage(Page):
    form_model = 'player'
    form_fields = ['verkaufA', 'kaufA', 'verkaufB', 'kaufB']

    def error_message(self, values):
        if values['kaufA'] + values['kaufB'] > self.player.endowment:
            return 'Ihre Nachfrage darf Ihr verfügbares Vermögen nicht übersteigen!'
        if values['verkaufA'] > 0 and self.player.anzahlA == 0:
            return 'Sie können keine A Aktie verkaufen, da Sie keine A Aktie im Portfolio haben.'
        if values['verkaufA'] <= values['kaufA']:
            return 'Ihr Angebot kann nicht über der Nachfrage liegen. Sie würden mit sich selber handeln.'
        if values['verkaufB'] > 0 and self.player.anzahlB == 0:
            return 'Sie können keine B Aktie verkaufen, da Sie keine B Aktie im Portfolio haben.'
        if values['verkaufB'] <= values['kaufB']:
            return 'Ihr Angebot kann nicht über der Nachfrage liegen. Sie würden mit sich selber handeln.'


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.verkaufA_liste()
        self.group.verkaufB_liste()
        self.group.kaufA_liste()
        self.group.kaufB_liste()
        self.group.datenA()
        self.group.datenB()
        self.group.rankA()
        self.group.rankB()
        self.group.marktpreisA_rech()
        self.group.marktpreisB_rech()
        self.group.handelA()
        self.group.handelB()
        self.group.ausfuhrung()
        self.group.dividende_rech()


class Results(Page):

    def vars_for_template(self):
        return {
            'verkaufA_liste': self.group.verkaufA_liste,
            'kaufA_liste': self.group.kaufA_liste,
            'marktpreisA': self.group.marktpreisA,
            'anzahlA': self.player.anzahlA,
            'endowment': self.player.endowment,
            'divA': self.group.dividendeA,
            'verkaufB_liste': self.group.verkaufB_liste,
            'kaufB_liste': self.group.kaufB_liste,
            'marktpreisB': self.group.marktpreisB,
            'anzahlB': self.player.anzahlB,
            'divB': self.group.dividendeB,
        }

class Ende(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self):
        return {
            'anzahlA': self.player.anzahlA,
            'anzahlB': self.player.anzahlB,
            'endowment': self.player.endowment,
        }


page_sequence = [Wait_Page, MyPage, ResultsWaitPage, Results, Ende]
