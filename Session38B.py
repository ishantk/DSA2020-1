"""
Fibonacci

0 1 1 2 3 5 8 13 . .....

0 1 2 3 4 5 6 7  . .....

1. Overlapping SubProblems
    when a sub problem solution is re computed several times
2. Optimal Sub Structure
   return fibonacci(number-1) + fibonacci(number-2)


Implementing TABULATION Method

"""

# Bottom Up Dynamic Programming Approach
def fibonacci(number):

    # Maintaining kind of Table
    dp = [0, 1]

    for i in range(2, number+1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[number]

def main():
    print(">> fibonacci(5) is:", fibonacci(5))
    print(">> fibonacci(7) is:", fibonacci(7))

if __name__ == '__main__':
    main()

# Compare running time of these programs and share across the group