from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import time

class PlayerBot(Bot):

    def play_round(self):
        yield pages.Welcome,
        yield pages.questions_pre, dict(gender= 1, year_of_birth= 1987, risk= 7)
        if self.participant.vars['treatment'] in Constants.baseline or self.participant.vars['treatment'] == 'Immediate_LowTax':
            if self.participant.vars['treatment'] not in Constants.deferred_group:
                yield pages.Instruction_Page, dict(comprehension_question1= 2, comprehension_question2= 0,
                                                   comprehension_question3= 0, comprehension_question4= 1,
                                                   comprehension_question5= 0, comprehension_question6= 0
                                                   ),
            elif self.participant.vars['treatment'] in Constants.deferred_group:
                yield pages.Instruction_Page, dict(comprehension_question1=2, comprehension_question2=0,
                                                   comprehension_question3=0, comprehension_question4=0,
                                                   comprehension_question5=1, comprehension_question6=0
                                                   ),
        else:
            yield pages.Instruction_Page, dict(comprehension_question1=2, comprehension_question2=0,
                                               comprehension_question3=0, comprehension_question4=0,
                                               comprehension_question5_2=1, comprehension_question6=0
                                               ),
        yield pages.comprehension_check



