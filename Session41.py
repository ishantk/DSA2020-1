"""

    Time Complexity Analysis :)

    We need it for an algorithm to understand in some simplified manner the below:
        worst case
        best case
        average case

    We may optimize algo or change the same in case our above expectations are not met

    simplified manner -> notations for these cases

    Big Oh -> O

    Rules:
    1. Ignore Constants
    O(n)    ->      5n

    2. Rule of Domiance
    O(1) < O(log n) < O(n) < O(n*n) < O(2 pow n) < O(n!)

    In case my algo is going to take constant time for few instructions
    and log n time for another few instruction
    So, we will choose -> O(long n) as our time complexity

    if x > 0:
        x = (x*2) + 10
        # O(1)
    elif x < 0:
        for i in range(1, 10):
            x += (x*i)
        # O(n)
    else:
        for i in range(1, 10):
            for j in range(1, 5):
                x += i*j
        # O(n*n)


    For above kind of solution we have time complexity as
    O(n*n)

    Worst Part for our Algo
    O(n*n)

"""

import matplotlib.pyplot as plt

# Relationship is Linear here :)
X = [1, 2, 3, 4, 5]
Y = [1, 2, 3, 4, 5]

plt.plot(X, Y)
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()

sum = 0
for i in range(1, 11):  # -> 10 times from 1 to 10
    sum += i            # -> 10 units of time

