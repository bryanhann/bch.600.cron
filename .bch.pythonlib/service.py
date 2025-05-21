#!/usr/bin/env python3
from pathlib import Path
import datetime
import time
import os

import scripting as SS
from util import say
from util import err
from util import backerr
from constants import ENV
from tools.poison import poisonpill

f_SERVING = ENV.f_SERVING
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
    backerr('bch.cron time_serve(): ' + hhmmss )


def runscript(script):
    os.chmod( str(script), 0o777 )
    print()
    print( f'=========={script}' )
    print( script.read_text() )
    print( '===========================================' )
    os.system( f'{script}' )
    print( f'=========={script}' )
    print()

def poll4dt(dt):
    header4dt(dt)
    acc = SS.matching_dt(dt)
    if acc:
        err('\n')
    for script in acc:
        err( f"    {script}\n" )
        newscript = script.parent/f'pending.{script.name}'
        script.rename(newscript)
        os.chmod( str(newscript), 0o777 )
        runscript(newscript)
        time.sleep(3)




def do_serve():
    while poisonpill():
        f_SERVING.touch()
        poll4dt( datetime.datetime.now())
        time.sleep(0.0)


if __name__ == '__main__':
    do_serve()

