#!/usr/bin/env python
"""Implementation of the Shamir secret sharing algorithm."""

import random
from Shamir import lagrange

# TODO Change this later
MAX = 257

def polynomial(coefficients, value):
    """ Calculates a single variable polynomial given the x balue.
    Uses the Horner method to avoid expensive exponentiation.

    coefficients: list; coefficients of the polynomial, in order of descending
        degree
    value: number; value to plug into the polynomial
    """
    result = 0
    for coefficient in coefficients:
        result = result * value + coefficient
    return result

def encode(secret, total, thresh):
    """ Encodes `secret` into `total` shares using the Shamir secret sharing
    method. Requires only `thresh` shares to reconstruct the original secret.

    secret: number; secret to split
    total: number; `n`, the total number of shares to generate
    thresh: number; `k`, the number of shares required to reconstruct the
        secret
    """
    rand = random.SystemRandom()
    coefficients = [rand.randint(0, MAX) for _ in range(thresh - 1)] \
        + [secret]
    return [
        [i + 1, polynomial(coefficients, i + 1)]
        for i in range(total)
    ]

def decode(shares):
    """ Attempts to reconstruct the original secret from `shares`.

    shares: list; list of at least `k` shares
    """
    return lagrange.construct(shares)

if __name__ == '__main__':
    # TODO Add cmd-line args
    print encode(5, 3, 2)
    print decode(encode(5, 3, 2))
