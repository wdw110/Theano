#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IPython Test Suite Runner.
"""
from __future__ import print_function


def main():
    # The tests can't even run if nose isn't available, so might as well  give the
    # user a civilized error message in that case.

    try:
        import nose
    except ImportError:
        error = """\
    ERROR: The IPython test suite requires nose to run.

    Please install nose on your system first and try again.
    For information on installing nose, see:
    http://nose.readthedocs.org/en/latest/

    Exiting."""
        import sys
        print(error, file=sys.stderr)
    else:
        import theano
        theano.test()

if __name__ == "__main__":
    main()
