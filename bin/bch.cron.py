#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "typer",
# ]
# ///

import sys
from pathlib import Path
from typing import List
from typing_extensions import Annotated

import typer

LIB = Path(__file__).parent/'lib'
sys.path.insert(0, str(LIB) )

import service as SERVICE
import scripting as SCRIPTING
import timing as TIMING
import alarm as ALARM
app = typer.Typer()

@app.command()
def at( time, cmd: List[str] ):
    SCRIPTING.do_script( time, ' '.join(cmd) )
    #SERVICE.do_at( time, ' '.join(cmd) )

@app.command()
def serve():
    SERVICE.do_serve()

@app.command()
def clear():
    SERVICE.do_clearscripts()

@app.command()
def alarm():
    ALARM.do_alarm()

@app.command()
def codes():
    ALARM.print_codes()

@app.command()
def answer(code):
    SCRIPTING.do_answer(code)

@app.command()
def matches(target):
    print(SERVICE.matches(target))


#3@app.command()
#def stat(): CC.killer() or CC.say( 'alive' )
#@app.command()
#def unstop(): CC.unstop() #STOP.exists() and STOP.unlink()
#@app.command()
#def stop(): CC.stop()
#@app.command()
#def show(): [ print(m) for m in CC.window() ]

if __name__ == '__main__':
    app()
