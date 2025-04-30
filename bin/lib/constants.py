#!/usr/bin/env python3

from pathlib import Path

CROND=Path.home()/'CRON.d'

CROND.is_dir() or CROND.mkdir()
