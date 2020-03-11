
def countAndSort(numbers, place):
    print("~~~~~~~countAndSort Start Place:[{}]~~~~~~~~~".format(place))
    print(">> Count And Sort numbers:", numbers, "place:", place)

    # Initial Lists with data as 0
    frequencyList = [0] * 10
    sortedList = [0] * len(numbers)

    for i in range(len(numbers)):
        num = numbers[i] // place
        index = num % 10
        frequencyList[index] += 1

    print("Frequency List:", frequencyList)

    print("Updating FrequencyList by Adding Previous Element")

    for i in range(1, len(frequencyList)):
        frequencyList[i] = frequencyList[i] + frequencyList[i-1]

    print("New Frequency List:", frequencyList)

    print("Put Data in sortedList by Referring FrequencyList")

    print("Put Data of sortedList in numbers")
    for i in range(len(numbers)):
        numbers[i] = sortedList[i]
    print("numbers sorted after place {} are {}".format(place, numbers))



    print("~~~~~~~~~countAndSort Finish~~~~~~~~~~~")
    print()

def radixSort(numbers):

    maxNumber = max(numbers)

    # print(maxNumber // 1)
    # print(maxNumber // 10)
    # print(maxNumber // 100)
    # print(maxNumber // 1000) -> 0 for maxNumber of 3 digit

    # countAndSort(numbers, 1)
    # countAndSort(numbers, 10)
    # countAndSort(numbers, 100)

    place = 1

    while maxNumber // place > 0:
        countAndSort(numbers, place)
        place *= 10


numbers = [901, 716, 232, 111, 201, 354, 676]

print("Original Numbers:", numbers)
print()
radixSort(numbers)
print()
print("Sorted Numbers:", numbers)
