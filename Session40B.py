"""

    Given dictionary of words and a word

    dictionaryOfWords = ["this", "th", "is", "famous", "Word",
                         "break", "b", "r", "e", "a", "k",
                         "br", "bre", "brea", "ak", "problem"]

    word = "Wordbreakproblem"


    Determine of word can be segmented into a space separated
    sequence of one or more dictionary words
    Word b r e a k problem
    Word br e a k problem
    Word br e ak problem
    .
    ..
    ....
"""

# Implement the same program with dpCache :)
def wordBreak(dictionaryOfWords, inputWord, output=""):

    if len(inputWord) == 0:
        print(output)
        return

    for i in range(1, len(inputWord)+1):

        prefix = inputWord[0:i]
        # print(prefix)

        if prefix in dictionaryOfWords:
            out = "{} {}".format(output, prefix)
            wordBreak(dictionaryOfWords, inputWord[i:], out)

def main():

    dictionaryOfWords = ["this", "th", "is", "famous", "Word",
                         "break", "b", "r", "e", "a", "k",
                         "br", "bre", "brea", "ak", "problem"]

    word = "Wordbreakproblem"

    wordBreak(dictionaryOfWords, word)

if __name__ == '__main__':
    main()