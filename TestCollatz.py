#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, compute_cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read2 (self) :
        r = StringIO.StringIO("9999999 1\n")
        a = [9999999, 1]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  9999999)
        self.assert_(a[1] == 1)

    def test_read3 (self) :
        r = StringIO.StringIO("1337 1337\n")
        a = [1337, 1337]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1337)
        self.assert_(a[1] == 1337)

    # ----
    # cycle_length
    # ----

    def test_compute_cycle_length_1 (self) :
        v = compute_cycle_length(1)
        self.assert_(v == 1)

    def test_compute_cycle_length_2 (self) :
        v = compute_cycle_length(2)
        self.assert_(v == 2)

    def test_compute_cycle_length_3 (self) :
        v = compute_cycle_length(3)
        self.assert_(v == 8)

    def test_compute_cycle_length_4 (self) :
        v = compute_cycle_length(100000)
        self.assert_(v == 129)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_char (self) :
        w = StringIO.StringIO()
        collatz_print(w, 'a', 'b', 'c')
        self.assert_(w.getvalue() == "a b c\n")

    def test_print_chardigitfloat (self) :
        w = StringIO.StringIO()
        collatz_print(w, 'a', 0, 4.5)
        self.assert_(w.getvalue() == "a 0 4.5\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("1 1\n2 2\n1 2\n2 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n1 2 2\n2 1 2\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("1 9999\n9999 10001\n99999 100000\n999999 1000000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 9999 262\n9999 10001 180\n99999 100000 227\n999999 1000000 259\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
