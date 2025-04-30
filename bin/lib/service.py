#!/usr/bin/env python3
from pathlib import Path
import datetime
import time
import os
from poison import poisonpill
#import timing as TT
import scripting as SS
import util as UU
from util import say

def do_at(time, cmd):
    SS.do_at4time4cmd(time,cmd)

def do_answer(code):
    SS.script4answer(code).touch()


def do_clearscripts():
    for script in SS.scripts():
        print( f'clear script {script}' )
        script.unlink()

def header4dt(dt):
    hhmmss = dt.strftime('%H:%M:%S')
    #hhmmss = TT.hhmmss4dt(dt)
    UU.backerr('bch.cron time_serve(): ' + hhmmss )


def poll4dt(dt):
    header4dt(dt)
    acc = SS.matching_dt(dt)
    if acc:
        UU.err('\n')
    for script in acc:
        UU.err( f"    {script}\n" )
        newscript = script.parent/f'pending.{script.name}'
        script.rename(newscript)
        os.system( f'{newscript} &' )




def do_serve():
    while poisonpill():
        poll4dt( datetime.datetime.now())
        time.sleep(0.0)


if __name__ == '__main__':
    do_serve()

