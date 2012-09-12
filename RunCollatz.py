#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
# EID   : rp22566
# CSID  : rprater
# CS373 - Downing - Project #1
# ---------------------------

"""
To run the program
    % python RunCollatz.py < RunCollatz.in > RunCollatz.out
    % chmod ugo+x RunCollatz.py
    % RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
