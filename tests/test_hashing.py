
import os
import subprocess
import tempfile

from souma import hashing


def test_hashing():
    '''Create lots of temporary file and compare the SHA512SUM file generated with sha512sum cli utility'''
    tmpdir = tempfile.TemporaryDirectory()
    filenames = [ os.path.join(tmpdir.name, 'file'+str(x)) for x in range(10) ]
    for fn in filenames:
        with open(fn, 'wb') as fd:
            fd.write(os.urandom(67*512))

    sha = hashing.ShaSumFile()
    for fn in filenames:
        sha.hashfile(fn)
    sha.genfile(tmpdir.name)
    shasumfile = os.path.join(tmpdir.name, 'SHA512SUM')

    cmd = ['sha512sum', '-c', shasumfile]
    done = subprocess.run(cmd, cwd=tmpdir.name)
    done.check_returncode()

    with open(shasumfile, 'r', encoding='utf-8') as fd:
        if sha.genstr() != fd.read():
            raise ValueError('genstr() and genfile() creates different output!')
