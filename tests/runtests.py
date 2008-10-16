#!/usr/bin/env python

import os
import subprocess
import sys

from alexs_lang.interpreter import Interpreter

def main():
    import alexs_lang
    directory = os.path.join(os.path.dirname(alexs_lang.__file__),'../tests/')
    executable = os.path.join(os.path.dirname(alexs_lang.__file__), 'al.py')
    failed = []
    tests = (os.path.join(directory, x) for x in os.listdir(directory) if x.endswith('.al'))
    if sys.argv[1:]:
        tests = (x for x in tests if os.path.splitext(os.path.basename(x))[0] in sys.argv[1:])
    for f in tests:
        p = subprocess.Popen([executable, f], stdout=subprocess.PIPE)
        try:
            assert p.stdout.read() == open("%sout" % f[:-2]).read()
            sys.stdout.write('.')
        except AssertionError:
            sys.stdout.write('F')
            failed.append(os.path.basename(f[:-3]))
        sys.stdout.flush()
    print
    if failed:
        print "The following tests failed:"
        print '\n'.join(failed)
    else:
        print "All tests passed"

if __name__ == '__main__':
    main()
