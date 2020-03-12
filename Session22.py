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



"""