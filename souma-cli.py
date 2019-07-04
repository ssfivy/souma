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
    import hashlib
    import json
    import subprocess
    import tarfile
    import tempfile
    import time
    cmd = ['journalctl', '--no-pager', '--output=short-iso', '-b -0'] # for now, only dump last boot
    done = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    with tarfile.open(args.file, 'a:') as tf:
        with tempfile.NamedTemporaryFile() as tfd:
            tfd.write(done.stdout)
            tfd.flush()
            tf.add(tfd.name, 'syslog.txt')

    metadata = {}
    metadata['fileversion'] = 1
    metadata['creationtime'] = time.time()
    m = hashlib.sha512()
    with tarfile.open(args.file, 'a:') as tf:
        with tempfile.NamedTemporaryFile() as tfd:
            s = json.dumps(metadata, indent=1, sort_keys=True).encode('utf-8')
            m.update(s)
            tfd.write(s)
            tfd.flush()
            tf.add(tfd.name, 'metadata.json')

    row = m.digest().hex() + '  metadata.json\n'
    b = row.encode('utf-8')

    m = hashlib.sha512()
    m.update(done.stdout)
    row = m.digest().hex() + '  syslog.txt\n'
    b += row.encode('utf-8')

    with tarfile.open(args.file, 'a:') as tf:
        with tempfile.NamedTemporaryFile() as tfd:
            tfd.write(b)
            tfd.flush()
            tf.add(tfd.name, 'SHA512SUM')


elif args.command == 'extract':
    # TODO: Spin off into modules
    import tarfile
    with tarfile.open(args.file, 'r') as tf:
        # FIXME: Vulnerable to zip bombs!
        tf.extractall()

