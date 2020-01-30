"""
    Search:
        1. Linear Search
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 50

# if element in numbers:
#     print(">> Element {} Found".format(element))

isElementFound = False

for i in range(0, len(numbers)):    # n
    if numbers[i] == element:       # 1
        isElementFound = True       # 1
        break

if isElementFound:
    print(">> Element {} Found".format(element))
else:
    print(">> Element {} NOT Found".format(element))

# Time Complexity | O(n)