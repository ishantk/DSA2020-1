"""
Subset Sum

A = [7, 3, 2, 5, 8]
subsets which makes 10 : [7, 3] and [8 and 2] and [2, 3, 5]
sum = 10
output: True

"""

# Brute Force Technique

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


def main():
    A = [7, 3, 2, 5, 8]
    sum = 14
    print("Output:", subsetSum(A, len(A)-1, sum))


if __name__ == '__main__':
    main()