#!/usr/bin/env python

import os
import subprocess

from alexs_lang.interpreter import Interpreter

def main():
    import alexs_lang
    directory = os.path.join(os.path.dirname(alexs_lang.__file__),'../tests/')
    executable = os.path.join(os.path.dirname(alexs_lang.__file__), 'al.py')
    failed = []
    for f in (os.path.join(directory, x) for x in os.listdir(directory) if x.endswith('.al')):
        p = subprocess.Popen([executable, f], stdout=subprocess.PIPE)
        try:
            assert p.stdout.read() == open("%sout" % f[:-2]).read()
            print '.',
        except AssertionError:
            print 'F',
            failed.append(os.path.basename(f[:-3]))
    print
    if failed:
        print "The following tests failed:"
        print '\n'.join(failed)
    else:
        print "All tests passed"

if __name__ == '__main__':
    main()
