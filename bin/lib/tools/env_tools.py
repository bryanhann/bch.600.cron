#!/usr/bin/env python3

import os
from pathlib import Path



def env(name):
    acc = {}
    name = name + '_'
    for key,val in environ.items():
        if key.startswith(name):
            shortkey = key[len(name):]
            acc[ shortkey ] = val
    for k in acc:
        if k.startswith('f_'):
            acc[k] = f_( acc[k] )
        if k.startswith('d_'):
            acc[k] = d_( acc[k] )
    return Environment(acc)

#
class Environment:
    def __init__(self, env):
        self.__env = env
    def __getattr__(self, name):
        return self.__env[name]
    def __repr__(self):
        pairs = [ repr(pair) for pair in self.__env.items() ]
        return '\n\t'.join([''] + pairs)
    def _dump(self):
        print('ENVIRONMENT:')
        width = max(len(k) for k in self.__env.keys() )
        for k,v in self.__env.items():
            print('\t', k.ljust(width), repr(v))
# Environment variables are of the form
#
#    BCH_CRON_f_<name> -- file
#    BCH_CRON_d_<name> -- direcory
#    BCH_CRON_<name>   -- other
#
# If a file or a directory, coerce the variable value
# to a Path object. If a directory, create it.
#

def get(name):
    val = os.environ[ f'BCH_CRON_{name}' ]
    if name.startswith('_f_'): val = _f_(val)
    if name.startswith('_d_'): val = _d_(val)


def get(name):
    val = os.environ[ f'BCH_CRON_{name}' ]
    if name.startswith('_f_'): val = _f_(val)
    if name.startswith('_d_'): val = _d_(val)

def f_(val):
    val = Path(val)
    return val

def d_(val):
    val = Path(val)
    val.is_dir() or val.mkdir()
    return val


#!/usr/bin/env python3
from os import environ

