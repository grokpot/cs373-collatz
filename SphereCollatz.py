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
# compute_cycle_length
# ------------

# Define the size of the cache
# Sphere results:
# size = 100        time limit exceeded
# size = 1000       time limit exceeded
# size = 10000      time ~ 7.2
# size = 100000     time ~ 1.53 <- best after extended testing
# size = 1000000    time ~ 1.98
# size = 2000000    time ~ 2.50
CACHE_SIZE = 100000
cache = [-1] * CACHE_SIZE

def compute_cycle_length (i):
    """
    This is a recursive method that computes the cycle length of i
    i is an int in which the cycle length is computed
    On the way back up from the base case, the cycles are added to the total (called cycle_length)
    """

    # Make sure we're computing the cycle length of a valid number
    assert i > 0

    global cache, CACHE_SIZE
    cycle_length = -1

    if (i < CACHE_SIZE) and (cache[i] != -1):
        cycle_length += (cache[i] + 1)
    else:
        # Base case. Cycle length of 1 is 1
        if (i == 1):
            cycle_length = 1
        # If i is even
        elif ((i % 2) == 0):
            cycle_length = (compute_cycle_length(i/2) + 1)
        # Else i is odd
        else:
            cycle_length = (compute_cycle_length(3*i + 1) + 1)
            # Cache the value if it's in our cache range
        if (i < CACHE_SIZE):
            cache[i] = cycle_length

    # Make sure cycle_length has changed from its instantiation
    assert cycle_length > 0

    return cycle_length



# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    # Beginning assertions
    assert i > 0
    assert j > 0

    max_cycle_length = -1

    # Sets the parameters in the right order for Python range()
    # Builds cache which is an array with indicies of n and values of cycle length(n)
    if i < j+1:
        n_range = range(i, j+1)
    else:
        n_range = range(j, i+1)

    # loops through given range
    for n in n_range:
        cycle_length = compute_cycle_length(n)

        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length

    # Ending assertions
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