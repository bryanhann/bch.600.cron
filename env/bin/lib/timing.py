#!/usr/bin/env python3

import time
import datetime
import hashlib

from util import COMMA, say, announce
from util import file_remove
from util import msloop

from tools.poison import poisonpill

from scripting import matching_answers
from constants import ENV

CROND = ENV.d_CROND
ANSWERED = ENV.f_ANSWERED



def __test():
    assert int4dd('00') == 0
    assert int4dd('05') == 5
    assert int4dd('12') == 12
    assert dd4int(0) == '00'
    assert twelve4hhmm( "11:xx" ) == "11:xx"
    assert twelve4hhmm( "12:xx" ) == "00:xx"
    print( 'test passed' )
    print_codes()

##########################################################################

def dd4int(x):
    return str(x+100)[-2:]
def int4dd(dd):
    assert len(dd)==2
    if dd[0] == '0':
        dd = dd[1]
    return int(dd)

def twelve4hhmm(hhmm):
    hh,mm = hhmm.split(':')
    assert len(hh) == 2
    hh = dd4int(int4dd(hh) % 12)
    return f"{hh}:{mm}"

def now():
    return datetime.datetime.now()

def hhmm4dt(dt):
    return dt.strftime('%H:%M')

def hhmmss4dt(dt):
    return dt.strftime('%H:%M:%S')

def phones4dt(dt):
    hhmm=hhmm4dt(dt)
    hh, mm = hhmm.split(':')
    return f"{hh} {mm} {COMMA}"

def code4hhmm(hhmm):
    hhmm = twelve4hhmm(hhmm)
    m = hashlib.md5()
    m.update( hhmm.encode() )
    return m.hexdigest()

def code4dt(dt):
    return code4hhmm(hhmm4dt(dt))
'''

#########################################################
def do_alarm(msg='deedoo'):
    do_alarm_first()
    now = datetime.datetime.now()
    code = code4dt(now)
    for ii in msloop(sec=3):
        poisonpill()
        if ii % 3000 == 0:
            print()
            announce( phones4dt(now), msg)
            print(code)
        if matching_answers(code):
            break
    do_alarm_last()

def do_alarm_first():
    file_remove(ANSWERED)

def do_alarm_last():
    say('answered')
    ANSWERED.touch()
'''

if __name__ == "__main__":
    __test()

