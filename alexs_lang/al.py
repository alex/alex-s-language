#!/usr/bin/env python

import sys

from alexs_lang.interpreter import Interpreter

if __name__ == '__main__':
    if sys.argv[1:]:
        Interpreter(open(sys.argv[1]).read()).execute()
