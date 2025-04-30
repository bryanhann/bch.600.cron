#!/usr/bin/env python3

import os
from pathlib import Path

from constants import CROND


def scripts():
    return sorted(list(CROND.glob('*')))

def matching_dt(dt):
    hhmmss = dt.strftime('%H:%M:%S')
    return [x for x in scripts() if hhmmss.startswith(x.name)]

def do_script(time,cmd):
    NEWLINE = '\n'
    script = CROND/time
    script.touch()
    script.write_text( script.read_text() + cmd + NEWLINE )
    os.chmod(script, 0o777)

def answers():
    return filter( None,  map( answer4script, scripts() ))

def matching_answers(target):
    return [x for x in answers() if target.startswith(x)]

def script4answer(answer):
    return CROND/f'answer.{answer}'

def answer4script(script):
    name = script.name + '..'
    if name.startswith('answer.'):
        return name.split('.')[1]

def do_answer(code):
     script4answer(code).touch()

