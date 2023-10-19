from functools import cache

@cache
def latticePaths(n, m):
    if (n == 0) | (m == 0):
        return 1
    return latticePaths((n - 1), m) + latticePaths(n, (m - 1))


if __name__ == "__main__":
    print(latticePaths(20, 20))
