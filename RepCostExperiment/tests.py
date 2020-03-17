from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random
import time

class PlayerBot(Bot):
    def play_round(self):
        if self.player.id_in_group == 1:
            yield pages.MyPage, dict(verkaufA=random.randrange(6,8,1), kaufA=random.randrange(8,10,1))
        if self.player.id_in_group == 2:
            yield pages.MyPage, dict(verkaufA=random.randrange(1,2,1), kaufA=random.randrange(2,6,1))
        if self.player.id_in_group == 3:
            yield pages.MyPage, dict(verkaufA=random.randrange(1,6,1), kaufA=random.randrange(4,10,1))
        time.sleep(40)


