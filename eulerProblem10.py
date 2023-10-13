'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

# Eartusnes Seive
def ESeive(upperBound):
    nums = [True] * upperBound
    nums[0] = nums[1] = False
    for idx in range(2,upperBound):
        if nums[idx]:
            yield idx
            for i in range(idx*2, upperBound, idx):
                nums[i] = False


if __name__ == "__main__":
    print(sum(ESeive(2_000_000)))
