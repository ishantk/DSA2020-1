"""
    https://www.mathsisfun.com/

    How to Code ?
    We have a Problem !! Write down data and solution !!
    x -> 2
    y -> 5
    solution:
    result -> 2 power 5
              2 * 2 * 2 * 2 * 2
              may or may not strike

    Always use functional approach to solve your problem
    And Remember inputs and outputs[is always returned]
"""

def power(x, y):

    result = 1                      # 1

    for i in range(0, y):           # n times
        result = result * x         # 1

    return result                   # 1

# 1 + n(1) + 1 -> n + 2
# T -> n+2

print(power(2, 5))
# How can this be managed in less than linear may be logarithmic


