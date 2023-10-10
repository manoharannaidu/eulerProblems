"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th
prime is 13. What is the 10001st prime number?
"""

# Imports
from math import log, ceil


# Upper limit of nth prime
def nthPrimeUpperBound(n):
    if n <= 6:
        return 15
    return ceil(n * (log(n) + log(log(n))))


# Sieve of Eratosthenes
def eratosthenesSeive(upperBound):
    numsTillUpperbound = [True] * (upperBound + 1)
    numsTillUpperbound[0] = numsTillUpperbound[1] = False
    for idx, isPrime in enumerate(numsTillUpperbound):
        if isPrime:
            yield idx
            for n in range((idx * 2), (upperBound + 1), idx):
                numsTillUpperbound[n] = False


if __name__ == "__main__":
    N = 10001
    primes = list(eratosthenesSeive(nthPrimeUpperBound(N)))
    print(primes[N - 1])
