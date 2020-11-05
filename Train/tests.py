from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random
import time

class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield pages.Welcome,
            yield pages.questions_pre, dict(seat_number= 1)
            yield pages.Instruction_Training
            yield pages.Probe
        #time.sleep(2)
        yield pages.Try1, dict(try_kauf=random.randrange(1, 10, 1), try_verkauf= random.randrange(11, 15, 1))
        #time.sleep(2)
        yield pages.Try2
        if self.round_number == Constants.num_rounds:
            #time.sleep(10)
            yield pages.Train_Ende


