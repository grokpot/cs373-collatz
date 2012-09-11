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

CACHE_SIZE = 1000000
cache = []

def compute_cycle_length (i):
    global cache, CACHE_SIZE
    cycle_length = -1

    if (i < CACHE_SIZE) and (cache[i] != -1):
        cycle_length += (cache[i] + 1)
    else:
        # Base case. Cycle length of 1 is 1
        if (i == 1):
            cycle_length = 1
        # If i is even
        elif (i % 2):
            cycle_length = (compute_cycle_length(i/2) + 1)
        # Else i is odd
            cycle_length = (compute_cycle_length(3*i + 1) + 1)
        # Cache the value if it's in our cache range
            cache[i] = cycle_length
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
        cache = [-1] * (j+1)
    else:
        n_range = range(j, i+1)
        cache = [-1] * (i+1)

    # TODO: try caching everything, even intermediate values, up to 1,000,000 (? possible ?)

    # loops through given range
    for n in n_range:
        # collatz is our 'intermediate-value'
        collatz = n
        # inclusive start
        cycle_length = 1

        while collatz > 1:
            # if collatz is even
            if collatz % 2 == 0:
                collatz /= 2
            # otherwise collatz is odd
            else:
                collatz = (3 * collatz)+ 1
                # inclusive end

            if collatz in n_range:
                if cache[collatz] != -1:
                    cycle_length += cache[collatz]
                    break

            cycle_length += 1

        cache[n] = cycle_length

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