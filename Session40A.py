"""
Subset Sum : Implement Dynamic Programming

A = [7, 3, 2, 5, 8]
subsets which makes 10 : [7, 3] and [8 and 2] and [2, 3, 5]
sum = 10
output: True

"""

import time

# Brute Force Technique + Dynamic Programming

def subsetSum(A, n, sum):

    # return true if sum is 0 (subset will be found)
    # base case
    if sum == 0:
        return True

    # base case : no items left or may be sum becomes negative
    if n < 0 or sum < 0:
        return False

    # Case1: Inclusion
    # Include current item in subset of A[n] and recursively solve the same
    # But for remaining n-1
    includeResult = subsetSum(A, n-1, sum-A[n])

    # Case2 Exclusion
    # Exclude current item in subset of A[n] and recursively solve the same
    # But for remaining n-1
    excludeResult = subsetSum(A, n-1, sum)

    # return true in case we find the sum in subset either including or excluding
    return includeResult or excludeResult


def subsetSumWithDP(A, n, sum, dpCache):

    # return true if sum is 0 (subset will be found)
    # base case
    if sum == 0:
        return True

    # base case : no items left or may be sum becomes negative
    if n < 0 or sum < 0:
        return False

    # You need to choose key which must be unique
    key = "{}-{}".format(n, sum)

    # No need to re-compute
    if key in dpCache:
        return dpCache[key]


    # Case1: Inclusion
    # Include current item in subset of A[n] and recursively solve the same
    # But for remaining n-1
    includeResult = subsetSumWithDP(A, n-1, sum-A[n], dpCache)

    # Case2 Exclusion
    # Exclude current item in subset of A[n] and recursively solve the same
    # But for remaining n-1
    excludeResult = subsetSumWithDP(A, n-1, sum, dpCache)

    # return true in case we find the sum in subset either including or excluding
    dpCache[key] = includeResult or excludeResult
    return dpCache[key]


def main():

    # A = [7, 3, 2, 5, 8]
    # sum = 14
    #

    A = [7, 3, 2, 5, 8]
    sum = 14
    # Dictionary : Key Value Pair | Read Operation -> O(1)
    dpCache = {}


    startTime1 = time.time()
    print("Output:", subsetSum(A, len(A) - 1, sum))
    endTime1 = time.time()

    startTime2 = time.time()
    print("Output:", subsetSumWithDP(A, len(A) - 1, sum, dpCache))
    endTime2 = time.time()

    print("Times:", endTime1-startTime1, endTime2-startTime2)


if __name__ == '__main__':
    main()