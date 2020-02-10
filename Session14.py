def bubbleSort(numbers):

    print(">> Length of Numbers:", len(numbers))

    for i in range(len(numbers)):
        print(">> i is:", i)
        for j in range(0, len(numbers)-i-1):
            print(j, end=" ")
            if numbers[j] > numbers[j+1]:
                # temp = numbers[j]
                # numbers[j] = numbers[j+1]
                # numbers[j+1] = temp
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        print()

numbers = [-3, 10, 14, -9, 11, 13]
bubbleSort(numbers)
print(numbers)
