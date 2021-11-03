from otree.api import Currency as c, currency_range
from . import *
from otree.api import Bot

import random
import time

class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield Welcome,
            yield questions_pre, dict(seat_number= 1)
            yield Instruction_Training
            yield Probe
        #time.sleep(2)
        yield Try1, dict(try_kauf=random.randrange(1, 10, 1), try_verkauf= random.randrange(11, 15, 1))
        #time.sleep(2)
        yield Try2
        if self.round_number == Constants.num_rounds:
            #time.sleep(10)
            yield Train_Ende


