#!/usr/bin/env python3

# Interface to journalctl
# Note this module API may change in the future

import subprocess

def get_all_today():
    '''Get all syslog from today'''
    cmd = ['journalctl', '--no-pager', '--output=short-iso', '-b -0'] # for now, only dump last boot
    done = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    done.check_returncode()
    return done.stdout
