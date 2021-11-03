from otree.api import Currency as c, currency_range
from . import *
from otree.api import Bot

import random
import time

class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            if self.player.rand == 1:
                    yield Instruction_Page, dict(comprehension_question2= 0,
                                                       comprehension_question3= 0, comprehension_question4= 1,
                                                       comprehension_question5= 1, comprehension_question6= 2
                                                       ),
            else:
                yield Instruction_Page, dict(comprehension_question2=0,
                                                   comprehension_question3=0, comprehension_question4=1,
                                                   comprehension_question5_2=2, comprehension_question6=2
                                                   ),
            yield comprehension_check
        if self.round_number == Constants.sequence_length + 1:
            yield New_Sequence
        #time.sleep(4)
        if self.player.id_in_group == 1:
            time.sleep(100)
            if self.player.anzahlA != 0 and self.player.anzahlB != 0:
                yield MyPage2, dict(verkaufA =random.randrange(31, 50, 1) , kaufA= random.randrange(1, 29, 1), verkaufB=random.randrange(31, 50, 1) , kaufB=random.randrange(1, 30, 1) )
            else:
                yield MyPage2, dict(verkaufA =None, kaufA= random.randrange(1, 29, 1), verkaufB=None, kaufB=random.randrange(1, 30, 1) )
        if self.player.id_in_group == 2:
            if self.player.anzahlA != 0 and self.player.anzahlB != 0:
                yield MyPage2, dict(verkaufA=random.randrange(31, 50, 1) , kaufA= random.randrange(1, 29, 1), verkaufB=random.randrange(31, 50, 1) , kaufB=random.randrange(1, 30, 1) )
            else:
                yield MyPage2, dict(verkaufA=None, kaufA= random.randrange(1, 29, 1), verkaufB=None, kaufB=random.randrange(1, 30, 1) )
        if self.player.id_in_group == 3:
            if self.player.anzahlA != 0 and self.player.anzahlB != 0:
                yield MyPage2, dict(verkaufA=random.randrange(16, 30, 1) , kaufA= random.randrange(1, 15, 1), verkaufB=random.randrange(16, 50, 1) , kaufB=random.randrange(1, 15, 1) )
            else:
                yield MyPage2, dict(verkaufA=None, kaufA= random.randrange(1, 15, 1), verkaufB=None, kaufB=random.randrange(1, 15, 1) )
        if self.player.id_in_group == 4:
            if self.player.anzahlA != 0 and self.player.anzahlB != 0:
                yield MyPage2, dict(verkaufA=random.randrange(16, 30, 1) , kaufA= random.randrange(1, 15, 1), verkaufB=random.randrange(16, 50, 1) , kaufB=random.randrange(1, 15, 1) )
            else:
                yield MyPage2, dict(verkaufA=None, kaufA= random.randrange(1, 15, 1), verkaufB=None, kaufB=random.randrange(1, 15, 1) )
        if self.player.id_in_group == 5:
            if self.player.anzahlA != 0 and self.player.anzahlB != 0:
                yield MyPage2, dict(verkaufA=random.randrange(46, 50, 1) , kaufA= random.randrange(1, 45, 1), verkaufB=random.randrange(46, 50, 1) , kaufB=random.randrange(1, 45, 1) )
            else:
                yield MyPage2, dict(verkaufA=None, kaufA= random.randrange(1, 45, 1), verkaufB=None, kaufB=random.randrange(1, 45, 1) )
        if self.player.id_in_group == 6:
            if self.player.anzahlA != 0 and self.player.anzahlB != 0:
                yield MyPage2, dict(verkaufA=random.randrange(46, 50, 1) , kaufA= random.randrange(1, 45, 1), verkaufB=random.randrange(46, 50, 1) , kaufB=random.randrange(1, 45, 1) )
            else:
                yield MyPage2, dict(verkaufA=None, kaufA= random.randrange(1, 45, 1), verkaufB=None, kaufB=random.randrange(1, 45, 1) )
        #time.sleep(4)
        yield Results2

        if self.subsession.func_period() == Constants.sequence_length:
            time.sleep(10)
            yield Ende
        if self.round_number == Constants.num_rounds:
            time.sleep(10)
            yield Uebersicht


