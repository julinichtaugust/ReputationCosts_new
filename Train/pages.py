from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#translations
def trans_question_incorrectly(number):
    return ('Frage {} wurde falsch beantwortet.').format(number)

class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1


class questions_pre(Page):
    form_model = 'player'


    def get_form_fields(self):
        return ['seat_number']

    def is_displayed(self):
        return self.round_number == 1

    def risk_error_message(self, value):
        if value == None:
            return "Diese Frage wurde nicht beantwortet."

class Instruction_Training(Page):
    form_model = 'player'

    #def get_form_fields(self):
     #   if self.player.rand == 1:
     #       return ['train_question1']
     #   else:
     #       return ['train_question1']

    def is_displayed(self):
        return self.round_number == 1

    #def train_question1_error_message(self, value):
    #    if value != 1:
    #        self.player.train_wrong_answer1 += 1
    #        return trans_question_incorrectly(1)

class Probe(Page):

    def is_displayed(self):
        return self.round_number == 1



#######################################################################################################
class Try1(Page):
    form_model = 'player'
    form_fields = ['try_verkauf', 'try_kauf']

    def is_displayed(self):
        if self.round_number == 1:
            return self.round_number == 1
        else:
            if self.round_number != 1:
                self.player.access_data()
                return self.round_number == 2

    def error_message(self, values):
        if values['try_kauf'] is None:
            pass
        else:
            if values['try_kauf']  > self.player.try_endowment:
                return 'Die Nachfrage darf Ihr verfügbares Vermögen nicht übersteigen!'

        if values['try_kauf'] is None or values['try_verkauf'] is None:
            pass
        else:
            if values['try_verkauf'] <= values['try_kauf']:
                return 'Ihre Nachfrage kann nicht über dem Angebot liegen. Sie würden mit sich selber handeln.'


    def before_next_page(self):
        self.player.set_value_try_verkauf()
        self.player.set_value_try_kauf()


class Try2(Page):

    def vars_for_template(self):
            return {
                'try_verkauf_liste': self.player.try_verkauf_liste,
                'try_kauf_liste': self.player.try_kauf_liste,
                'try_marktpreis': self.player.try_marktpreis,
                'try_anzahl': self.player.try_anzahl,
                'try_endowment': self.player.try_endowment,
                'try_dividende': self.player.try_dividende,
                'try_daten_verkauf': self.player.try_daten_verkauf,
                'try_daten_kauf': self.player.try_daten_kauf,
                'try_verkauf_liste_h': self.player.try_verkauf_liste_h,
                'try_kauf_liste_h': self.player.try_kauf_liste_h,
                'try_rank':self.player.try_rank,
                'try_rank_verkauf_player': self.player.try_rank_verkauf_player,
                'try_rank_kauf_player': self.player.try_rank_kauf_player,
                'try_marktpreis_rech': self.player.try_marktpreis_rech,
                'try_handel': self.player.try_handel,
                'try_ausfuhrung': self.player.try_ausfuhrung,
                'try_vermogen': self.player.try_vermogen,
            }

class Train_Ende(Page):

    def is_displayed(self):
        if self.round_number == 2:
            return self.round_number == 2

    def vars_for_template(self):
            return {
                'try_verkauf_liste': self.player.try_verkauf_liste,
                'try_kauf_liste': self.player.try_kauf_liste,
                'try_marktpreis': self.player.try_marktpreis,
                'try_anzahl': self.player.try_anzahl,
                'try_endowment': self.player.try_endowment,
                'try_dividende': self.player.try_dividende,
                'try_daten_verkauf': self.player.try_daten_verkauf,
                'try_daten_kauf': self.player.try_daten_kauf,
                'try_verkauf_liste_h': self.player.try_verkauf_liste_h,
                'try_kauf_liste_h': self.player.try_kauf_liste_h,
                'try_rank':self.player.try_rank,
                'try_rank_verkauf_player': self.player.try_rank_verkauf_player,
                'try_rank_kauf_player': self.player.try_rank_kauf_player,
                'try_marktpreis_rech': self.player.try_marktpreis_rech,
                'try_handel': self.player.try_handel,
                'try_ausfuhrung': self.player.try_ausfuhrung,
                'try_vermogen': self.player.try_vermogen,
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