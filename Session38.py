"""
Fibonacci

0 1 1 2 3 5 8 13 . .....

0 1 2 3 4 5 6 7  . .....

1. Overlapping SubProblems
    when a sub problem solution is re computed several times
2. Optimal Sub Structure
   return fibonacci(number-1) + fibonacci(number-2)


"""

def fibonacci(number):

    if number<2:
        return number

    print(">> Evaluating fibonacci({}) + fibonacci({})".format(number-1, number-2))
    return fibonacci(number-1) + fibonacci(number-2)

def main():
    print(">> fibonacci(5) is:", fibonacci(5))
    # print(">> fibonacci(7) is:", fibonacci(7))

if __name__ == '__main__':
    main()