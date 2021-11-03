from otree.api import Currency as c, currency_range
from . import *
from otree.api import Bot

import time
from otree.api import Submission


class PlayerBot(Bot):

    def play_round(self):
        yield questions1, dict(gender=0,age=18, abschluss=1, fakultaet=1, familie=1, kinder=1, income=1)
        yield questions2, dict(kenntnis=1, geldanlagen=1, risiko_allgemein=1, risiko=1, schlupf=1, hinterziehen=1, leistungen=1, sinnvoll=1, hybrid=1, lizenz=1, privilegien=1, oase=1, treaty=1, handelsblatt=1, bild=1, spiegel=1, welt=1, zeit=1, focus=1, mm=1, regio=1, sonsZ=1, sparen=1, verteilung=1, umgebung_hint=1, umgebung_schl=1, akzeptanz_hint=1, akzeptanz_schl=1, aufdeckung=1, interpretation=1, respekt=1, fair=1, strafen=1, aktien=1, politik=1)
        yield questions3, dict(gründung=1, aufwand=1, doppelt=1, kinderarbeit=1)
        yield questions4, dict(erklaerung='So weit',anmerkungen='So gut')

        #yield Submission(payment, check_html=False)
        #yield payment, dict(anmerkungen= 'Das war super!')
        #time.sleep(30)  # 1 = 1 second

