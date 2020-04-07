"""

    Dynamic Programming - II
    KnapScak Problem Statement

    > Memoization
    > Tabulation

"""

# Brute Force Solution
# Basic Recursive Solution

def knapSack(profits, weights, capacity):
    return knapSackSolution(profits, weights, capacity, 0)


def knapSackSolution(profits, weights, capacity, currentIndex):

    # Base Conditions for Stopping Your recursive Program
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # We need to compute 2 profits
    # 1 by selecting the element another by skipping the element

    # By Selecting the Element at current Index
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapSackSolution(profits, weights, capacity - weights[currentIndex], currentIndex+1)

    # By Excluding the Element at Current Index
    profit2 = knapSackSolution(profits, weights, capacity, currentIndex+1)

    return max(profit1, profit2)


def main():
    # profits = [1, 6, 10, 16]
    # weights = [1, 2, 3, 5]
    # capacity = 7

    profits = [4, 5, 3, 7]
    weights = [2, 3, 1, 4]
    capacity = 5

    maxProfit = knapSack(profits, weights, capacity)
    print(">> Max Profit for Profits:{} with Weights:{} for Capacity:{} is:{}"
          .format(profits, weights, capacity, maxProfit))


if __name__ == '__main__':
    main()