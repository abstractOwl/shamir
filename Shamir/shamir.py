#!/usr/bin/env python
"""Implementation of the Shamir secret sharing algorithm."""

import random
from . import lagrange

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
    if thresh > total:
        raise ValueError("threshold value [%d] exceeds total value [%d]"
                         % (thresh, total))

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

def main():
    """ Main function """
    choice = raw_input("[?] Split or combine a secret? [split/combine] ")

    print

    if choice == "split":
        secret = int(raw_input("[?] Enter secret: "))
        total = int(raw_input("[?] Enter number of shares: "))
        thresh = int(raw_input("[?] Enter threshold value: "))

        out = encode(secret, total, thresh)

        print
        print "[*] Printing shares:"
        for x_val, y_val in out:
            print " -- D[%2d]: (%2d, %d)" % (x_val - 1, x_val, y_val)

        print
        if total <= 10:
            # WolframAlpha seems to give up after degree 10 polynomial
            print "[*] See polynomial at:"
            y_vals = [y_val for _, y_val in out]
            url = "http://www.wolframalpha.com/input/?i="
            print url + "%2B".join([
                ("%dx%%5E%d" % (y_val, len(y_vals) - i - 1))
                for i, y_val in enumerate(y_vals)
            ])

    elif choice == "combine":
        total = int(raw_input("[?] Number of shares: "))
        points = []

        for _ in range(total):
            point = raw_input("[?] Enter comma-separated pair: ").split(",")
            points.append([int(x) for x in point])

        print
        print "[*] The secret is %d." % decode(points)

    else:
        print "[!] ERROR: Invalid choice."

if __name__ == '__main__':
    main()

