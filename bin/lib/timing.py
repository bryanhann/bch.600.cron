#!/usr/bin/env python3
import time
import datetime
import hashlib
from poison import poisonpill

from util import COMMA, say, announce
from scripting import matching_answers

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
    m = hashlib.md5()
    m.update( hhmm.encode() )
    return m.hexdigest()

def code4dt(dt):
    return code4hhmm(hhmm4dt(dt))

def do_alarm(msg='deedoo'):
    now = datetime.datetime.now()
    code = code4dt(now)
    while matching_answers(code) == []:
        poisonpill()
        announce( phones4dt(now), msg)
        print(code)
        time.sleep(1)
    say( 'answered' )
