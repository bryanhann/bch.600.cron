#!/usr/bin/env python3
import time
import os
from pathlib import Path

POISONPILL = Path.home()/'die'

from util import say

def _poisononpill_set( msg='poisoned' ):
    POISONPILL.write_text(msg)

def _poisonpill_clear():
    POISONPILL.exists() and POISONPILL.unlink()

def _poisonpill_exists():
    return POISONPILL.exists()

def _poisonpill_exit():
    if _poisonpill_exists():
         say( "poison" )
         exit( "poison" )

def poisonpill(seconds=0):
    _poisonpill_exit()
    for ii in range(seconds*10):
        _poisonpill_exit()
        print('.',)
        time.sleep(0.1)
    return True
def poisoned():
    return POISONPILL.exists()


