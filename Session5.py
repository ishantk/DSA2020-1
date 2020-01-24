"""
def fun():
    print("This is fun")

def show():
    print("This is Awesome")
    fun()
    printNum("Bye")
    # return -> Termination of Function
"""

# for i in range(1, 11, 2):
#     print(">> i is:", i)

def printNum(num):

    print(">> num is:", num)
    num = num - 1

    if num == 0:
        return

    # Recursion : Execute a function from a function
    printNum(num)  # Tail Recursion
    return


printNum(10)

# 10 9 8 7 6 5 4 3 2 1

