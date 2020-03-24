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
    form_fields = ['verkaufA', 'kaufA']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.verkaufA_liste()
        self.group.kaufA_liste()
        self.group.daten()
        self.group.rank()
        self.group.marktpreisA_rech()
        self.group.handelA()
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
        }

class Ende(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def vars_for_template(self):
        return {
            'anzahlA': self.player.anzahlA,
            'endowment': self.player.endowment,
        }


page_sequence = [Wait_Page, MyPage, ResultsWaitPage, Results, Ende]
