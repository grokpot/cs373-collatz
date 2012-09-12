#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
# EID   : rp22566
# CSID  : rprater
# CS373 - Downing - Project #1
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
CACHE_SIZE = 100000
cache = [-1] * CACHE_SIZE
ONE_CYCLE = 1
TWO_CYCLES = 2

def compute_cycle_length (current_num):
    """
    This is a recursive method that computes the cycle length of current_num
    current_num is an int in which the cycle length is computed
    On the way back up from the base case, the cycles are added to the total (called cycle_length)
    """

    # Make sure we're computing the cycle length of a valid number
    assert current_num > 0
    # Make sure we're getting an int
    assert isinstance(current_num, int)

    global cache, CACHE_SIZE
    cycle_length = -1

    # If the current num is within the cache list index and has been cached
    if (current_num < CACHE_SIZE) and (cache[current_num] != -1):
        cycle_length += (cache[current_num] + ONE_CYCLE)
    # Otherwise recurse
    else:
        # Base case. Cycle length of 1 is 1
        if (current_num == 1):
            cycle_length = 1
        # If current_num is even
        elif ((current_num % 2) == 0):
            # Determine cycle length of current_num by recursively sending n/2
            cycle_length = (compute_cycle_length(current_num/2) + ONE_CYCLE)
        # Else current_num is odd
        else:
            # Determine cycle length of current_num by recursively sending (3n+1)/2
            # NOTE: This is a shortcut. Since an odd * odd = even, we can combine steps here (as opposed to sending 3n+1 and then n/2 in the next step).
            cycle_length = (compute_cycle_length(current_num + (current_num >> 1) + 1) + TWO_CYCLES)
            # Cache the value if it's in our cache range
        if (current_num < CACHE_SIZE):
            cache[current_num] = cycle_length

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
    # pre-condition assertions
    assert i > 0
    assert j > 0
    # Make sure we're getting ints
    assert isinstance(i, int)
    assert isinstance(j, int)

    max_cycle_length = -1

    # Sets the parameters in the right order for Python range()
    # Builds cache which is an array with indicies of n and values of cycle length(n)
    if i < j+1:
        n_range = range(i, j+1)
    else:
        n_range = range(j, i+1)

    # Make sure we've got a valid range
    assert isinstance(n_range, list)

    # loops through given range
    for n in n_range:
        cycle_length = compute_cycle_length(n)

        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length

    # post-condition assertions
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