"""
Fibonacci

0 1 1 2 3 5 8 13 . .....

0 1 2 3 4 5 6 7  . .....

1. Overlapping SubProblems
    when a sub problem solution is re computed several times
2. Optimal Sub Structure
   return fibonacci(number-1) + fibonacci(number-2)


Implementing MEMOIZATION method

"""

def fibonacci(number):

    # Cache for our program
    memory = [-1 for n in range(number+1)]
    return calculateFibonacci(memory, number)


def calculateFibonacci(memory, number):

    if number<2:
        return number

    # In case we have earlier solved a problem, you give a solution from our memory cache
    if memory[number] >= 0:
        print(">> Returning Result for calculateFibonacci({})".format(memory[number]))
        return memory[number]

    print(">> Evaluating calculateFibonacci({}) + calculateFibonacci({})".format(number - 1, number - 2))
    memory[number] = calculateFibonacci(memory, number-1) + calculateFibonacci(memory, number-2)
    return memory[number]

def main():
    print(">> fibonacci(5) is:", fibonacci(5))
    # print(">> fibonacci(7) is:", fibonacci(7))

if __name__ == '__main__':
    main()


"""
Before DP Implementation
>> Evaluating fibonacci(4) + fibonacci(3)
>> Evaluating fibonacci(3) + fibonacci(2)
>> Evaluating fibonacci(2) + fibonacci(1)
>> Evaluating fibonacci(1) + fibonacci(0)
>> Evaluating fibonacci(1) + fibonacci(0)
>> Evaluating fibonacci(2) + fibonacci(1)
>> Evaluating fibonacci(1) + fibonacci(0)
>> fibonacci(5) is: 5

After DP Implementation
>> Evaluating calculateFibonacci(4) + calculateFibonacci(3)
>> Evaluating calculateFibonacci(3) + calculateFibonacci(2)
>> Evaluating calculateFibonacci(2) + calculateFibonacci(1)
>> Evaluating calculateFibonacci(1) + calculateFibonacci(0)
>> Returning Result for calculateFibonacci(1)
>> Returning Result for calculateFibonacci(2)
>> fibonacci(5) is: 5
"""