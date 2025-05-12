#!/usr/bin/env python3

import time
import datetime
import hashlib
from tools.poison import poisonpill

from util import COMMA, say, announce
from scripting import matching_answers
#from constants import CROND
#from constants import ANSWERED
from constants import ENV
CROND=ENV.d_CROND
ANSWERED = ENV.f_ANSWERED
import timing as TT
from util import msloop
def __msloop(sec=1):
    factor = 1000
    while True:
        for ii in range(int(sec*factor)):
            yield ii
            time.sleep(1/factor)

def do_alarm(msg='deedoo'):
    do_alarm_first()
    now = datetime.datetime.now()
    code = TT.code4dt(now)
    for ii in msloop(sec=3):
        poisonpill()
        if ii % 3000 == 0:
            print()
            announce( TT.phones4dt(now), msg)
            print(code)
        if matching_answers(code):
            break
    do_alarm_last()

def do_alarm_first():
    ANSWERED.exists() and ANSWERED.unlink()

def do_alarm_last():
    say('answered')
    ANSWERED.touch()

def print_codes():
    for h in range(24):
        for m in range(0,60,10):
            hh = dd4int(h)
            mm = dd4int(m)
            hhmm = f"{hh}:{mm}"
            if m==0:
                print()
                if h%3 == 0: print()
                print( hhmm, end = ' ||   ', )
            print( TT.code4hhmm(hhmm)[:2], end=" -- " )

