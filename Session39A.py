"""

    Dynamic Programming - II
    KnapScak Problem Statement

    > Memoization Technique
"""

def knapSack(profits, weights, capacity):

    # Create Memoization Cache for the Solution
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]

    # Pass the Cache as 1st input itself
    return knapSackSolution(dp, profits, weights, capacity, 0)


def knapSackSolution(dp, profits, weights, capacity, currentIndex):

    # Base Conditions for Stopping Your recursive Program
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # In case we have a solution already existing for us, use the same and return from here
    # no need to do further computation
    if dp[currentIndex][capacity] != -1:    # O(1)
        return dp[currentIndex][capacity]

    # We need to compute 2 profits
    # 1 by selecting the element another by skipping the element

    # By Selecting the Element at current Index
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapSackSolution(dp, profits, weights, capacity - weights[currentIndex], currentIndex+1)

    # By Excluding the Element at Current Index
    profit2 = knapSackSolution(dp, profits, weights, capacity, currentIndex+1)

    # Saving results in Cache O(1)
    dp[currentIndex][capacity] = max(profit1, profit2)

    return dp[currentIndex][capacity]


def main():
    profits = [1, 6, 10, 16]
    weights = [1, 2, 3, 5]
    capacity = 7

    # profits = [4, 5, 3, 7]
    # weights = [2, 3, 1, 4]
    # capacity = 5

    maxProfit = knapSack(profits, weights, capacity)
    print(">> Max Profit for Profits:{} with Weights:{} for Capacity:{} is:{}"
          .format(profits, weights, capacity, maxProfit))



    """
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]

    for row in dp:
        print(row)
    """


if __name__ == '__main__':
    main()