#!/usr/bin/env python3

# CLI launcher for souma

# Initialisation
################
import argparse

# Argument parsing
##################
helptext = 'souma-cli - dump system information, or read the dumpfile'
parser = argparse.ArgumentParser(description=helptext)
subparsers = parser.add_subparsers(help='command', dest='command')
subparsers.required = True

sparser = subparsers.add_parser('dump', help='Dump system information to a dumpfile')
sparser.add_argument('file', action='store', help='Filename of dumpfile ')

sparser = subparsers.add_parser('extract', help='Extract information from a dumpfile')
sparser.add_argument('file', action='store', help='Dumpfile to extract')

args = parser.parse_args()

# Input processing
##################
if args.command == 'dump':
    # TODO: Spin off into modules
    import subprocess
    import tarfile
    import tempfile
    cmd = ['journalctl', '--no-pager', '--output=short-iso', '-b -0'] # for now, only dump last boot
    done = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    with tempfile.NamedTemporaryFile() as tfd:
        tfd.write(done.stdout)
        with tarfile.open(args.file, 'w') as tf:
            tf.add(tfd.name, 'syslog.txt')

elif args.command == 'extract':
    # TODO: Spin off into modules
    import tarfile
    with tarfile.open(args.file, 'r') as tf:
        # FIXME: Vulnerable to zip bombs!
        tf.extractall()

