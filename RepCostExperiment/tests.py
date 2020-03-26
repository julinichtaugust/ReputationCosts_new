from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random
import time

class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group == 1:
            yield pages.MyPage, dict(verkaufA=random.randrange(8, 10, 1), kaufA= random.randrange(5, 8, 1), verkaufB=random.randrange(8, 10, 1), kaufB=random.randrange(5, 7, 1))
        if self.player.id_in_group == 2:
            yield pages.MyPage, dict(verkaufA=random.randrange(4, 5, 1), kaufA=random.randrange(1, 4, 1), verkaufB=random.randrange(3, 6, 1), kaufB=random.randrange(1, 2, 1))
        if self.player.id_in_group == 3:
            yield pages.MyPage, dict(verkaufA=random.randrange(6, 10, 1), kaufA=random.randrange(5, 6, 1), verkaufB=random.randrange(6, 10, 1), kaufB=random.randrange(1, 5, 1))
        time.sleep(10)
        yield pages.Results
        if self.round_number == Constants.num_rounds:
            time.sleep(10)
            yield pages.Ende


