"""
def mergeSort(numbers):
    left = []
    right= []

    mid = (0 + len(numbers)-1)//2
    print(mid)

    for i in range(0, mid):
        left.append(numbers[i])

    for i in range(mid, len(numbers)):
        right.append(numbers[i])

    print(left)
    print(right)

    print(numbers[0:mid])
    print(numbers[mid:len(numbers)])

"""

def merge(numbers, left, middle, right):
    print("==MERGE START==")
    # print(numbers, left, middle, right)


    leftSize = middle - left + 1     # Size of Left List
    rightSize = right - middle       # Size of Right List
    print("LEFT SIZE:", leftSize, "RIGHT SIZE:", rightSize)

    # Creating SubLists | Left and Right
    leftList = numbers[0: leftSize]
    rightList = numbers[middle+1: rightSize+1]

    print("[LEFT LIST:]", leftList)
    print("[RIGHT LIST:]", rightList)
    print("==MERGE FINISH==")

def mergeSort(numbers, left, right):


    if left < right:

        middle = (left+right)//2
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("[Numbers]:", numbers[left:right+1])
        print("[MIDDLE]:", middle, "[LEFT]:", left, "[RIGHT]:", right)
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        mergeSort(numbers, left, middle)            # Left Sub List
        mergeSort(numbers, middle+1, right)         # Right Sub List

        merge(numbers, left, middle, right)

numbers = [-3, 10, 14, -9, 11, 13, 2]
print("[NUMBERS]:",numbers)


mergeSort(numbers, 0, len(numbers)-1)
print(numbers)
