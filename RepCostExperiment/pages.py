from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#translations
def trans_question_incorrectly(number):
    return ('Frage {} wurde falsch beantwortet.').format(number)



class Instruction_Page(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.player.rand == 1:
            return ['comprehension_question2', 'comprehension_question3',
                    'comprehension_question4', 'comprehension_question5', 'comprehension_question6']
        else:
            return ['comprehension_question2', 'comprehension_question3',
                    'comprehension_question4', 'comprehension_question5_2', 'comprehension_question6']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            sequence=self.subsession.func_sequence(),
            periode=self.subsession.func_period()
        )
        #context =  self.player.vars_for_template()
        #context.update(
        #    image_path12_LifeCycle = ('graphics/12_periods/LifeCycle.png').format(self.round_number),
        #    image_path12_income= ('graphics/12_periods/LifeCycleIncome.png').format(self.round_number),
        #    image_path12_rest= ('graphics/12_periods/LifeCycle_RestPhase.png').format(self.round_number),
        #    image_path12_questionnaire= ('graphics/12_periods/LifeCycle_Questionnaire.png').format(self.round_number),
        #    image_path12_payoff= ('graphics/12_periods/LifeCycle_Payoff.png').format(self.round_number),
        #    image_path12_test= ('graphics/12_periods/LifeCycle_ComprehensionTest.png').format(self.round_number),
        #)
        #return context

    #def comprehension_question1_error_message(self, value):
    #    if value != 2:
    #        self.player.wrong_answer1 += 1
    #        return trans_question_incorrectly(1)

    def comprehension_question2_error_message(self, value):
        if value != 0:
            self.player.wrong_answer2 += 1
            return trans_question_incorrectly(1)

    def comprehension_question3_error_message(self, value):
            if value != 0:
                self.player.wrong_answer3 += 1
                return trans_question_incorrectly(2)

    def comprehension_question4_error_message(self, value):
            if value != 1:
                self.player.wrong_answer4 += 1
                return trans_question_incorrectly(3)

    def comprehension_question5_error_message(self, value):
        if value != 1:
            self.player.wrong_answer5 += 1
            return trans_question_incorrectly(4)

    def comprehension_question5_2_error_message(self, value):
        if value !=2:
            self.player.wrong_answer5_2 += 1
            return trans_question_incorrectly(4)

    def comprehension_question6_error_message(self, value):
            if value != 2:
                self.player.wrong_answer6 += 1
                return trans_question_incorrectly(5)



class comprehension_check(Page):

    def is_displayed(self):
        return self.round_number == 1

    def check_wrong_anwers(self):
        if self.player.rand == 1:
            if self.player.wrong_answer1 + self.player.wrong_answer2 + self.player.wrong_answer3 + self.player.wrong_answer4 + self.player.wrong_answer5 + self.player.wrong_answer6 >= 100:
                return False
            else:
                return True
        else:
            if self.player.wrong_answer1 + self.player.wrong_answer2 + self.player.wrong_answer3 + self.player.wrong_answer4 + self.player.wrong_answer5_2 + self.player.wrong_answer6 >= 100:
                return False
            else:
                return True

    def vars_for_template(self):
        context =  self.player.vars_for_template()
        context.update(
            comprehension_check= self.check_wrong_anwers(),
            wrong_answers= self.player.wrong_answer1 + self.player.wrong_answer2 + self.player.wrong_answer3 + self.player.wrong_answer4 + self.player.wrong_answer5 + self.player.wrong_answer6,

        )
        return context


#######################################################################################################
class New_Sequence(Page):
    def is_displayed(self):
        return self.round_number == Constants.sequence_length + 1

    def vars_for_template(self):
        return dict(
            sequence=self.subsession.func_sequence(),
            periode=self.subsession.func_period()
        )

class Wait_Page(WaitPage):
    def after_all_players_arrive(self):
        for player in self.group.get_players():
            if self.round_number != 1:
                player.access_data()
                player.access_seq_data()
            if self.round_number == Constants.sequence_length + 1:
                player.endowment = 1500
                player.anzahlA = 5
                player.anzahlB = 5



class MyPage2(Page):
    form_model = 'player'
    form_fields = ['verkaufA', 'kaufA', 'verkaufB', 'kaufB']

    def get_timeout_seconds(self):
        if self.round_number <= 3:
            second = 120
        else:
            second = 60
        return second

    def after_all_players_arrive(self):
        if self.subsession.func_period() >= 2:
            self.group.marktpreisA_alt()

    def vars_for_template(self):
        return dict(
            marktpreisA_alt= self.group.marktpreisA_alt(),
            marktpreisB_alt= self.group.marktpreisB_alt(),
            sequence= self.subsession.func_sequence(),
            periode= self.subsession.func_period()
        )

    def error_message(self, values):
        #print('values is', values)
        if values['kaufA'] is None:
            pass
        else:
            if values['kaufA'] > self.player.endowment:
                return 'Ihre Nachfrage darf Ihr verfügbares Vermögen nicht übersteigen!'
            else:
                pass

        if values['kaufB'] is None:
            pass
        else:
            if values['kaufB'] > self.player.endowment:
                return 'Ihre Nachfrage darf Ihr verfügbares Vermögen nicht übersteigen!'
            else:
                pass

        if values['kaufA'] is None or values['kaufB'] is None:
            pass
        else:
            if values['kaufA'] + values['kaufB'] > self.player.endowment:
                return 'Die Summe der Nachfragen der Aktien beider Unternehmen darf Ihr verfügbares Vermögen nicht übersteigen!'

        if values['verkaufA'] is None:
            pass
        else:
            if values['verkaufA'] > 0 and self.player.anzahlA == 0:
                if self.player.rand == 1:
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
            if values['verkaufB'] > 0 and self.player.anzahlB == 0:
                if self.player.rand == 1:
                    return 'Sie können keine B Aktie verkaufen, da Sie keine B Aktie im Portfolio haben.'
                else:
                    return 'Sie können keine A Aktie verkaufen, da Sie keine A Aktie im Portfolio haben.'

        if values['kaufB'] is None or values['verkaufB'] is None:
            pass
        else:
            if values['verkaufB'] <= values['kaufB']:
                return 'Ihre Nachfrage (= Kauf) kann nicht über oder gleich dem Angebot (= Verkauf) liegen. Sie würden mit sich selber handeln.'

    def before_next_page(self):
        self.player.set_value_verkaufA()
        self.player.set_value_verkaufB()
        self.player.set_value_kaufA()
        self.player.set_value_kaufB()

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.verkaufA_liste()
        self.group.verkaufB_liste()
        self.group.kaufA_liste()
        self.group.kaufB_liste()
        self.group.datenA_verkauf()
        self.group.datenA_kauf()
        self.group.rank_verkaufA()
        self.group.rank_kaufA()
        self.group.datenA_verkauf_liste()
        self.group.datenA_kauf_liste()
        self.group.datenB_verkauf()
        self.group.datenB_kauf()
        self.group.rank_verkaufB()
        self.group.rank_kaufB()
        self.group.datenB_verkauf_liste()
        self.group.datenB_kauf_liste()
        self.group.rankA()
        self.group.rankB()
        self.group.marktpreisA_rech()
        self.group.marktpreisB_rech()
        self.group.handelA()
        self.group.handelB()
        self.group.ausfuhrung()
        self.group.dividende_rech()





    


class Results2(Page):


    def get_timeout_seconds(self):
        if self.round_number <= 3:
            second = 120
        else:
            second = 60
        return second

    def vars_for_template(self):
            return {
                'verkaufA_liste': self.group.verkaufA_liste,
                'kaufA_liste': self.group.kaufA_liste,
                'marktpreisA': self.group.marktpreisA,
                'anzahlA': self.player.anzahlA,
                'endowment': self.player.endowment,
                'endowmentalt': self.player.endowmentalt,
                'divA': self.group.dividendeA,
                'gesdiviA': self.player.gesdiviA,
                'datenA_verkauf_liste': self.group.datenA_verkauf_liste,
                'verkaufB_liste': self.group.verkaufB_liste,
                'kaufB_liste': self.group.kaufB_liste,
                'marktpreisB': self.group.marktpreisB,
                'anzahlB': self.player.anzahlB,
                'divB': self.group.dividendeB,
                'gesdiviB': self.player.gesdiviB,
                'datenB_verkauf_liste': self.group.datenB_verkauf_liste,
                'dividende_rech': self.group.dividende_rech,
                'dividendeA': self.group.dividendeA,
                'dividendeB': self.group.dividendeB,
                'sequence': self.subsession.func_sequence(),
                'periode': self.subsession.func_period()
            }


class ResultsWaitPage2(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    def is_displayed(self):
        return self.subsession.func_period() == Constants.sequence_length


class Ende(Page):

    def is_displayed(self):
        return self.subsession.func_period() == Constants.sequence_length
    
    def vars_for_template(self):
        return {
            'anzahlA': self.player.anzahlA,
            'anzahlB': self.player.anzahlB,
            'endowment': self.player.endowment,
            'endowment_euro': self.player.endowment_euro,
            'endowment_ende': self.player.endowment_ende,
            'auszahlung_euro': self.player.auszahlung_euro,
            'part_fee': self.player.part_fee,
            'auszahlung': self.participant.payoff_plus_participation_fee(),
            'sequence': self.subsession.func_sequence(),
            'periode': self.subsession.func_period(),

        }



class Uebersicht(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'sequence': self.subsession.func_sequence(),
            'periode': self.subsession.func_period(),
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
    Uebersicht
   ]