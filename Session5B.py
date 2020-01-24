# Recursive Function to find max of number in list

def maxNumber(data, length):

    print(">> maxNumber executed with length[{}]".format(length))

    if length == 1:
        print(">> maxNumber returned {} with length[{}]".format(data[0], length))
        return data[0]
    else:
        num = maxNumber(data, length-1)

    if num > data[length-1]:
        print(">> maxNumber returned with length[{}]".format(length))
        return num
    else:
        print(">> maxNumber returned with length[{}]".format(length))
        return data[length-1]



numbers = [10, 11, 12]
print(">> Max is:", maxNumber(numbers, len(numbers)))

"""
def fun1():
    
    # Recursion
    # fun1()

    # InDirect Recursion
    fun2()
    
    print(">> fun1")

    # Tail Recursion
    # fun1()
    
def fun2():
    
    # fun1()

    fun2()
    
    print(">> fun2")

"""

# HW: Implement Recursion in Insertion Sort Algorithm

