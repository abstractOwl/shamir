#!/usr/bin/env python
""" Functions to construct a Lagrange polynomial from points """

def poly_mult(poly1, poly2):
    """
    Returns the product of two polynomial vectors

    poly1: list; First polynomial
    poly2: list; Second polynomial
    """
    # degree(PQ) = degree(P) + degree(Q)
    # -1 * 2 to account for x^0 in facors, + 1 for x^0 in result = -1
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]
    return result

def test_poly_mult():
    """ Unit test for poly_mult() """
    assert poly_mult([1, 3], [2, 4]) == [2, 10, 12]
    assert poly_mult([0], [1, 3, 4]) == [0, 0, 0]


def poly_add(poly1, poly2):
    """ Returns the sum of two polynomials.

    poly1: list; First polynomial to add
    poly2: list; Second polynomial to add
    """
    result = [0] * max(len(poly1 or []), len(poly2))
    # Add backwards in case of length mismatch
    for i in range(len(poly1)):
        result[-(i + 1)] += poly1[-(i + 1)]
    for i in range(len(poly2)):
        result[-(i + 1)] += poly2[-(i + 1)]
    return result

def test_poly_add():
    """ Unit test for poly_add() """
    assert poly_add([1, 2], [3, 4]) == [4, 6]
    assert poly_add([], [1, 2]) == [1, 2]
    assert poly_add([1, 2, 3], [5, 4]) == [1, 7, 7]


def construct(points):
    """ Constructs a polynomial from specified points.

    points: list; points to reconstruct the secret with
    """
    result = []
    for j in range(len(points)):
        poly = reduce(poly_mult, [[
            1.0                  / (points[j][0] - points[m][0]),
            (0.0 - points[m][0]) / (points[j][0] - points[m][0])
        ] for m in range(len(points)) if m != j])
        result.append([x * points[j][1] for x in poly])
    return reduce(poly_add, result)[-1]

def test_construct():
    """ Unit test for construct() """
    # First test from Wikipedia
    assert construct([[2, 1942], [4, 3402], [5, 4414]]) == 1234.0
    assert construct([[1, 39], [2, 73], [3, 107]]) == 5.0


if __name__ == '__main__':
    test_poly_mult()
    test_poly_add()
    test_construct()
    print "All unit tests passed"
