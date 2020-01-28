# https://visualgo.net/en/sorting

# Utility Function to get the minimum number's index
def getMinIdx(data, start, stop):

    minIdx = start

    for i in range(start, stop):
        if data[i] < data[minIdx]:
            minIdx = i

    return minIdx


def swapElements(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


def selectionSort(data):

    for i in range(0, len(data)):
        minIdx = getMinIdx(data, i, len(data))
        # print(">> Minimum Idex is:", minIdx)
        swapElements(data, minIdx, i)


numbers = [45, 22, 11, 23, 19, 10, 33, 12, 55, 66]
print("NUMBERS BEFORE: ")
print(numbers)

selectionSort(numbers)

print()
print("NUMBERS AFTER: ")
print(numbers)


# Implement Recursion somewhere here and thr :)
