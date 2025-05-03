#!/usr/bin/env python3

import sys
import os
import time

BACKSPACES = '\b' * 50
SPACE = ' '
COMMA = '.'

def err(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()

def backerr(msg):
    err( BACKSPACES + msg )

def lfilter(*a,**b):
    return list(filter(*a,*b))

def announce(*args):
    msg = SPACE.join(args)
    print(msg)
    say(msg)

def say(*args):
    msg = ' '.join(args)
    os.system( f'say {msg}' )


def file_remove(file):
    file.exists() and file.unlink()

def msloop(sec=1):
    factor = 1000
    while True:
        for ii in range(int(sec*factor)):
            yield ii
            time.sleep(1/factor)


