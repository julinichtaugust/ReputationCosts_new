from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

from django.utils.translation import ugettext_lazy as _

#translations
def trans_question_incorrectly(number):
    return _('Frage {} wurde falsch beantwortet.').format(number)

class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        context =  self.player.vars_for_template()
        context.update(
            mean_remuneration=c(Constants.mean_remuneration).to_real_world_currency(self.session),
        )
        return context

class questions_pre(Page):
    form_model = 'player'

    def get_form_fields(self):
        return ['gender', 'year_of_birth', 'risk']

    def is_displayed(self):
        self.participant.vars['year_of_birth'] = self.player.year_of_birth
        return self.round_number == 1

    def risk_error_message(self, value):
        if value == None:
            return "Diese Frage wurde nicht beantwortet."

class Instruction_Page(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.participant.vars['treatment'] in Constants.baseline or self.participant.vars['treatment'] == 'Immediate_LowTax':
            return ['comprehension_question1', 'comprehension_question2', 'comprehension_question3',
                    'comprehension_question4', 'comprehension_question5', 'comprehension_question6']
        else:
            return ['comprehension_question1', 'comprehension_question2', 'comprehension_question3',
                    'comprehension_question4', 'comprehension_question5_2', 'comprehension_question6']

    def is_displayed(self):
        self.player.treatment = self.participant.vars['treatment']
        return self.round_number == 1

    def vars_for_template(self):
        context =  self.player.vars_for_template()
        context.update(
            image_path12_LifeCycle = _('graphics/12_periods/LifeCycle.png').format(self.round_number),
            image_path12_income= _('graphics/12_periods/LifeCycleIncome.png').format(self.round_number),
            image_path12_rest= _('graphics/12_periods/LifeCycle_RestPhase.png').format(self.round_number),
            image_path12_questionnaire= _('graphics/12_periods/LifeCycle_Questionnaire.png').format(self.round_number),
            image_path12_payoff= _('graphics/12_periods/LifeCycle_Payoff.png').format(self.round_number),
            image_path12_test= _('graphics/12_periods/LifeCycle_ComprehensionTest.png').format(self.round_number),
            income1= self.participant.vars['income_list'][0],
            income2= self.participant.vars['income_list'][1],
            income3= self.participant.vars['income_list'][2],
            income4= self.participant.vars['income_list'][3],
        )
        return context

    def comprehension_question1_error_message(self, value):
        if value != 2:
            self.player.wrong_answer1 += 1
            return trans_question_incorrectly(1)

    def comprehension_question2_error_message(self, value):
        if value != 0:
            self.player.wrong_answer2 += 1
            return trans_question_incorrectly(2)

    def comprehension_question3_error_message(self, value):
            if value != 0:
                self.player.wrong_answer3 += 1
                return trans_question_incorrectly(3)

    def comprehension_question4_error_message(self, value):
            if value != 1 and self.participant.vars['treatment'] not in Constants.deferred_group:
                self.player.wrong_answer4 += 1
                return trans_question_incorrectly(4)
            elif value != 0 and self.participant.vars['treatment'] in Constants.deferred_group:
                self.player.wrong_answer4 += 1
                return trans_question_incorrectly(4)

    def comprehension_question5_error_message(self, value):
            if value != 0 and self.participant.vars['treatment'] not in Constants.deferred_group:
                self.player.wrong_answer5 += 1
                return trans_question_incorrectly(5)
            elif value != 1 and self.participant.vars['treatment'] in Constants.deferred_group:
                self.player.wrong_answer5 += 1
                return trans_question_incorrectly(5)

    def comprehension_question5_2_error_message(self, value):
            if value != 0 and self.participant.vars['treatment'] not in Constants.deferred_group:
                self.player.wrong_answer5 += 1
                return trans_question_incorrectly(5)
            elif value != 1 and self.participant.vars['treatment'] in Constants.deferred_group:
                self.player.wrong_answer5 += 1
                return trans_question_incorrectly(5)

    def comprehension_question6_error_message(self, value):
            if value != 0:
                self.player.wrong_answer6 += 1
                return trans_question_incorrectly(6)

class comprehension_check(Page):
    def check_wrong_anwers(self):
        if self.player.wrong_answer1 + self.player.wrong_answer2 + self.player.wrong_answer3 + self.player.wrong_answer4 + self.player.wrong_answer5 + self.player.wrong_answer6 >= 3:
            return False
        else:
            return True

    def vars_for_template(self):
        context =  self.player.vars_for_template()
        context.update(
            image_path12_test= _('graphics/12_periods/LifeCycle_ComprehensionTest.png').format(self.round_number),
            comprehension_check= self.check_wrong_anwers(),
            wrong_answers= self.player.wrong_answer1 + self.player.wrong_answer2 + self.player.wrong_answer3 + self.player.wrong_answer4 + self.player.wrong_answer5 + self.player.wrong_answer6,
        )
        return context

page_sequence = [
    Welcome,
    questions_pre,
    Instruction_Page,
    comprehension_check
]

import logging
#import otree.common_internal
# Get an instance of a logger
#logger = logging.getLogger(__name__)