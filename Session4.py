# Insertion Sort: Arrange data in Ascending Order
# https://visualgo.net/en/sorting

def insertionSort(data):

    for i in range(1, len(data)):        # n times

        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:     # n times
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key


numbers = [45, 22, 11, 23, 19, 10, 33, 12, 55, 66]
insertionSort(numbers)

# 45, 22, 11, 23, 19, 10, 33, 12, 55, 66  | Original Data

# i: 1 | j: 0 | key: 45
# 22, 45, 11, 23, 19, 10, 33, 12, 55, 66

# i: 2 | j: 1 | key: 11
# 22, 45, 11, 23, 19, 10, 33, 12, 55, 66

# 11, 22, 45, 23, 19, 10, 33, 12, 55, 66

for number in numbers:
    print(number, end=" < ")

