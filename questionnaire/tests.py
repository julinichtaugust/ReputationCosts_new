from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import time
from otree.api import Submission


class PlayerBot(Bot):

    def play_round(self):
        yield pages.questions1, dict(age= 32, job= 1, abschluss= 2, familie= 2, income= 3)
        yield pages.questions2, dict(taxaversion2= 0, taxcomplexity= 2, decision= 7, taxmoral= 1, taxaversion= 9, dread1= 500, dread2= 500, dread3= 500, debtaversion=1)
        yield pages.questions3, dict(crt_bat= 1.15, crt_widget= 1, crt_lake= 55)
        #yield Submission(pages.payment, check_html=False)
        #yield pages.payment, dict(anmerkungen= 'Das war super!')
        #time.sleep(30)  # 1 = 1 second

