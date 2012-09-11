#!/usr/bin/env python

# ---------------------------
# SphereCollatz.py
# Ryan Prater
# ---------------------------

# -------
# imports
# -------

import sys

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0

    max_cycle_length = -1

    # Sets the parameters in the right order for Python range()
    if i < j+1:
        index_range = range(i, j+1)
    else:
        index_range = range(j, i+1)

    # loops through given range
    for index in index_range:
        # collatz is our 'intermediate-value'
        collatz = index
        # inclusive start
        current_cycle_length = 1
        while collatz > 1:
            # if collatz is even
            if collatz % 2 == 0:
                collatz /= 2
            # otherwise collatz is odd
            else:
                collatz = (3 * collatz)+ 1
                # inclusive end
            current_cycle_length += 1
        if current_cycle_length > max_cycle_length:
            max_cycle_length = current_cycle_length
    assert max_cycle_length > 0
    return max_cycle_length

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)

collatz_solve(sys.stdin, sys.stdout)