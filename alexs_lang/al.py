#!/usr/bin/env python

from optparse import OptionParser
import os
import subprocess
import sys

from alexs_lang.compile import Compiler
from alexs_lang.interpreter import Interpreter


def main():
    parser = OptionParser()
    parser.add_option('-c', '--compile', action="store_true", dest='compile', help='compile the file')
    parser.add_option('-o', '--out', dest='file', help='location for generated c++ file if using the compile option')
    parser.add_option('-i', '--interpret', action="store_false", dest='compile', help='interpret the file')
    
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        raise SystemExit
    f = open(args[0]).read()
    if options.compile:
        out = options.file or 'a.cpp'
        Compiler(f, out).compile()
        subprocess.call(['indent', out])
        os.remove('%s~' % out)
    else:
        Interpreter(f).execute()

if __name__ == '__main__':
    main()
