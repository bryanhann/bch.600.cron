#!/usr/bin/env bash

head=$1
this=${BASH_SOURCE[0]}
lib=$(dirname $this)
root=$(dirname $lib)

__exp ()  { export ${head}_$1=$2; }
__path () { [[ ":$PATH:" == *":${1}:"* ]] || export PATH=${PATH}:${1} ; }

. $(dirname ${BASH_SOURCE[0]})/constants.sh

unset __exp
unset __path

