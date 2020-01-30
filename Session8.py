"""
    TIME COMPLEXITY
"""

# Redundant Checks
def isHavingPair(numbers, sum):

    hasPair = None

    for i in range(0, len(numbers)):

        for j in range(0, len(numbers)):

            if j == i:
                continue

            result = numbers[i] + numbers[j]

            if result == sum:
                hasPair = True
                break
            else:
                hasPair = False

        if hasPair:
            break

    return hasPair


# Unique Checks
def isHavingPair(numbers, sum):

    hasPair = None

    for i in range(0, len(numbers)):

        for j in range(i+1, len(numbers)):

            result = numbers[i] + numbers[j]

            if result == sum:
                hasPair = True
                print(">> Pair is: {} {}".format(numbers[i], numbers[j]))
                break
            else:
                hasPair = False

        if hasPair:
            break

    return hasPair


# Python Set Data Structure
# Retrieve operation on Set is O(1)
# Save complement of number with sum in set

def isHavingPair(numbers, sum):

    complements = set()
    for num in numbers:
        diff = sum - num
        if num in complements:
            return True
        else:
            complements.add(diff)

    return False


numbers1 = [1, 2, 3, 9]
numbers2 = [2, 4, 1, 4]
sum = 8

# -> num : 2 | C: 6 | S{6}
# -> num : 4 | C: 4 | S{6, 4}
# -> num : 1 | C: 7 | S{6, 4, 7}
# -> num : 4 | C: 4 | S{6, 4, 7}


# nums = {1, 2, 3, 4, 4}

print(numbers1, isHavingPair(numbers1, sum))
print()

print(numbers2, isHavingPair(numbers2, sum))

# Time Complexity -> O(n2)
# Reduce the Time Complexity to O(n) | it means use only 1 loop
# Add Mathematical Logic with Dynamic Programming Approach :)

