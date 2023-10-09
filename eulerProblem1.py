"""
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Imports
from math import floor


# Get sum of all multiples of a given number below another given number
def sumMulBelowN(N: int, x: int) -> int:
    """
    Sum all multiples of x below N
    param N:    The upper limit for multiples of x
    param x:    Number whose sum of multiples we need to find
    returns:    The sum of all multiples of x below N
    """
    mulx = floor((N - 1) / x)
    return x * (mulx * (mulx + 1) / 2)


if __name__ == "__main__":
    """
    Get sum of all multiples of 3 below 1000
    Get sum of all multiples of 5 below 1000
    Subtract sum of all multiples of 15 below 1000 since we counted these twice
    """
    N = 1000
    print(sumMulBelowN(N, 3) + sumMulBelowN(N, 5) - sumMulBelowN(N, 15))
