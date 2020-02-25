def mergeSort(numbers):

    # Firstly we shall Divide the Data into Left and Right
    if len(numbers) > 1:
        middle = len(numbers)//2
        leftList = numbers[0: middle]
        rightList = numbers[middle:]

        print("MERGE SORT: [LEFT]", leftList, "[RIGHT]", rightList)

        # Division of Lists

        #  Left List Sorting
        mergeSort(leftList)

        # Right List Sorting
        mergeSort(rightList)

        # Comparison of List Elements
        i = 0
        j = 0
        k = 0

        # To make sure data is sorted
        while i < len(leftList) and j < len(rightList):
            print("SORT WHILE EXECUTED | i: {}, j:{}, [LEFT]:{}, [RIGHT]:{}".format(i, j, leftList, rightList))
            if leftList[i] < rightList[j]:
                numbers[k] = leftList[i]
                i += 1
            else:
                numbers[k] = rightList[j]
                j += 1

            k += 1

        print("1. SORT WHILE LOOP RESULT | NUMBERS:{}".format(numbers))

        # Accommodate Remaining Elements
        while i < len(leftList):
            print("LEFT ACCOMMODATION | i:{}, k:{}".format(i, k))
            numbers[k] = leftList[i]
            i += 1
            k += 1

        print("2. LEFT WHILE LOOP RESULT | NUMBERS:{}".format(numbers))

        while j < len(rightList):
            print("RIGHT ACCOMMODATION | j:{}, k:{}".format(j, k))
            numbers[k] = rightList[j]
            j += 1
            k += 1

        print("3. RIGHT WHILE LOOP RESULT | NUMBERS:{}".format(numbers))

numbers = [-3, 10, 14, -9, 11, 13, 2]
print("[ORIGINAL NUMBERS]:", numbers)

mergeSort(numbers)
print("[SORTED NUMBERS]:", numbers)

