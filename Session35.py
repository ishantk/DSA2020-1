class TrieNode:

    def __init__(self, char):
        self.char = char
        self.children = []

        # Will set it to True, when word finishes
        self.isWordFinished = False

        # Number of times the same charctater in appears trie data structure
        self.count = 1


class Trie:

    def __init__(self):
        # Root Attribute of Trie is available in the Object
        self.root = TrieNode('*')
        print(">> Trie Data Structure Created with Root as *")

    # Acknowledge us with insertion results
    def add(self, word):

        node = self.root

        for char in word:
            # print(char)
            found = False
            for child in node.children:
                if child.char == char:
                    child.count += 1
                    node = child
                    found = True
                    break

            if not found:
                newAlphabetNode = TrieNode(char)
                node.children.append(newAlphabetNode)
                node = newAlphabetNode

        # Last Node must be end of word, signified by marking the isWordFinished to True
        node.isWordFinished = True



    # Returns True/False
    def search(self, word):

        node = self.root

        # In case Trie Data Structure is Empty :(
        if not self.root.children:
            return False

        # character by character traversal
        for char in word:
            charNotFound = True
            # iterate into list of children
            for child in node.children:
                if child.char == char:
                    charNotFound = False
                    node = child
                    break

            if charNotFound:
                return False

        return True

    # Return a List of words available from this word as prefix
    def hints(self, word):
        pass


def main():

    trie = Trie()
    trie.add("string")
    trie.add("stringify")
    trie.add("stringent")
    trie.add("strong")
    trie.add("straight")

    print(trie.search("stringent")) # T
    print(trie.search("str"))       # T
    print(trie.search("sia"))       # F
    print(trie.search("strong"))    # T
    print(trie.search("seek"))      # F


    print(trie.hints("stri"))   # string, stringify, stringent | All the words having string as prefix
    print(trie.hints("str"))    # all the words having str as prefix


if __name__ == '__main__':
    main()