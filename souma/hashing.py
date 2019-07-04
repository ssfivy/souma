#!/usr/bin/env python3

# Hashing-related stuff

import hashlib
import os

class ShaSumFile():
    '''Helper class to construct a checksum file'''
    def __init__(self, chunksize=10240):
        self.entries = {}
        self.chunksize = chunksize

    def hashbytes(self, filebytes, filename):
        '''Hashes a bunch of bytes that is the content of filename. Can be called iteratively'''
        if self.entries.get(filename) is None:
            self.entries[filename] = hashlib.sha512()
        self.entries[filename].update(filebytes)

    def hashfile(self, filepath):
        '''Hashes a file on disk (chunked)'''
        filename = os.path.basename(filepath)
        with open(filepath, 'rb') as fd:
            while True:
                data = fd.read(self.chunksize)
                if not data:
                    break
                self.hashbytes(data, filename)

    def genrow(self, filename):
        '''Generate a single row in SHASUM file'''
        return self.entries[filename].digest().hex() + '  {}\n'.format(filename)

    def genstr(self):
        '''Generate SHASUM file as a string'''
        rows = []
        for fn in sorted(self.entries):
            rows.append(self.genrow(fn))
        return ''.join(rows)

    def genfile(self, directory):
        '''Generate SHASUM file in a specific directory'''
        with open(os.path.join(directory, 'SHA512SUM'), 'w', encoding='utf-8') as fd:
            for fn in sorted(self.entries):
                fd.write(self.genrow(fn))


