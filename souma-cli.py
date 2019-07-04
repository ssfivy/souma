#!/usr/bin/env python3

# CLI launcher for souma

# Initialisation
################
import argparse

from souma import hashing
from souma import journal
from souma import metadata

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
    import tarfile
    import tempfile

    syslog = journal.get_all_today()

    sha = hashing.ShaSumFile()

    s = metadata.gen_metadata_v1_str().encode('utf-8')

    with tarfile.open(args.file, 'a:') as tf:
        with tempfile.NamedTemporaryFile() as tfd:
            tfd.write(syslog)
            tfd.flush()
            tf.add(tfd.name, 'syslog.txt')
            sha.hashbytes(syslog, 'syslog.txt')

    with tarfile.open(args.file, 'a:') as tf:
        with tempfile.NamedTemporaryFile() as tfd:
            tfd.write(s)
            tfd.flush()
            tf.add(tfd.name, 'metadata.json')
            sha.hashbytes(s, 'metadata.json')

    with tarfile.open(args.file, 'a:') as tf:
        with tempfile.NamedTemporaryFile() as tfd:
            tfd.write(sha.genstr().encode('utf-8'))
            tfd.flush()
            tf.add(tfd.name, 'SHA512SUM')


elif args.command == 'extract':
    # TODO: Spin off into modules
    import tarfile
    with tarfile.open(args.file, 'r') as tf:
        # FIXME: Vulnerable to zip bombs!
        tf.extractall()

