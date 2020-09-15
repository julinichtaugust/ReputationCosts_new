from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random
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

        time.sleep(1)
        if self.player.id_in_group == 1:
            yield pages.MyPage2, dict(verkaufA=random.randrange(8, 10, 1), kaufA= random.randrange(5, 8, 1), verkaufB=random.randrange(8, 10, 1), kaufB=random.randrange(5, 7, 1))
        if self.player.id_in_group == 2:
            yield pages.MyPage2, dict(verkaufA=random.randrange(4, 5, 1), kaufA=random.randrange(1, 4, 1), verkaufB=random.randrange(3, 6, 1), kaufB=random.randrange(1, 2, 1))
        if self.player.id_in_group == 3:
            yield pages.MyPage2, dict(verkaufA=random.randrange(6, 10, 1), kaufA=random.randrange(5, 6, 1), verkaufB=random.randrange(6, 10, 1), kaufB=random.randrange(1, 5, 1))
        time.sleep(10)
        yield pages.Results2
        if self.round_number == Constants.num_rounds:
            time.sleep(10)
            yield pages.Ende


