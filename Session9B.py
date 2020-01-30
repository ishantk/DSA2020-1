def generateCombinations(num):

    combinations = []

    for i in range(0, 2**num):
        combination = []

        for j in range(num-1, -1, -1):
            combination.append(i // 2**j % 2)

        # combination.append(i // 32 % 2)
        # combination.append(i // 16 % 2)
        # combination.append(i // 8 % 2)
        # combination.append(i // 4 % 2)
        # combination.append(i // 2 % 2)
        # combination.append(i % 2)

        # combination = "{} {} {} {}".format(i//8%2, i//4%2, i//2%2, i%2)

        combinations.append(combination)

    # combinations is a list of lists
    return combinations


combinations = generateCombinations(3)
for combination in combinations:
    print(combination)

