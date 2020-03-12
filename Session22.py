"""
    Apply Quick Sort
    numbers: 10, 88, 33, 99, 44, 57, 76
    indexes: 0, 1,   2,  3,  4,  5,  6
    low : 0
    high: len - 1

    pivot numbers[high] -> numbers[6]
    pivot : 76

    QS says, let 76 i.e. pivot be in the right position
    i.e. numbers lesser than 76 should be in left of it
    and numbers greater than 76 should be in right of it

    Algo:
    j = 0   | iterating from 0 to len-1
    for every j index we compare with pivot and do some swap operation
    i = -1

    j -> 0 numbers[0] -> 10
    if numbers[j] <= pivot | i+=1 | swap [numbers[i] and numbers[j]]
    i = 0 | Hence, no swapping can be done :(

    j -> 1 numbers[1] -> 88
    if numbers[j] <= pivot
    no swap

    j -> 2 numbers[2] -> 33
    if numbers[j] <= pivot | i+=1 | swap [numbers[i] and numbers[j]]
    i -> 1
    numbers: 10, 88, 33, 99, 44, 57, 76
    indexes: 0, 1,   2,  3,  4,  5,  6

    numbers: 10, 33, 88, 99, 44, 57, 76

    .
    ..
    ....

    when j:5
    numbers : 10, 33, 44, 57, 88, 99, 76

    Once Loop is finished, j shall be len-1 i.e. 6
    Here, we will place pivot at correct position by doing a swap
    on numbers[i+1] with numbers[len-1]

    when j:6 | swapping 88 and 76
    numbers : 10, 33, 44, 57, 88, 99, 76 -> numbers : 10, 33, 44, 57, 76, 99, 88
    76 is in the right position :)

"""

def partition(numbers, low, high):

    pivot = numbers[high]
    i = low - 1

    print("PARTITION START - NUMBERS:{} | LOW:{} |  HIGH:{}".format(numbers, low, high))
    print("PIVOT:{}".format(pivot))

    # Iterate for j = 0 to len -1
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            # Swap Numbers at i and j
            numbers[i], numbers[j] = numbers[j], numbers[i]

    # Once Loop terminates, we shall place pivot at correct position
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]

    print("PARTITION FINISH - NUMBERS:{} | LOW:{} |  HIGH:{} | i:{}".format(numbers, low, high, i))

    # Return the New Pivot or last element where i index stopped
    return i+1


def quickSort(numbers, low, high):

    if low < high:
        pivot = partition(numbers, low, high)
        quickSort(numbers, low, pivot-1)
        quickSort(numbers, pivot+1, high)




print(">> Original Numbers before Quick Sort:")
numbers= [10, 88, 33, 99, 44, 57, 76]
print(numbers)

quickSort(numbers, 0, len(numbers)-1)

print(">> Sorted Numbers after Quick Sort:")
print(numbers)