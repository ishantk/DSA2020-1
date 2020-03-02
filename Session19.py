import hashlib

class Word:

    def __init__(self, word):
        self.word = word
        self.frequency = 1

    def __str__(self):
        return "{} [{}]".format(self.word, self.frequency)

class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = []

        for _ in range(capacity):
            self.buckets.append(None)

        print(">> HASHTABLE CONSTRUCTED WITH CAPACITY [{}]".format(capacity))

    def hashCode(self, word):
        index = int(hashlib.sha512(word.encode("utf-8")).hexdigest(), 16) % self.capacity
        return index

    def put(self, word):

        index = self.hashCode(word.word.lower())

        if self.buckets[index] == None:
            self.buckets[index] = word
            self.size += 1
            print("^^ {} Inserted in HashTable".format(word.word))
        else:
            self.buckets[index].frequency += 1
            print("## {} Frequency Updated to {} in HashTable".format(word.word, word.frequency))

    def iterate(self):
        print("~~~~~~~~~~~~~~")
        for word in self.buckets:
            if word != None:
                print(word)
        print("~~~~~~~~~~~~~~")

    def get(self, word):
        index = self.hashCode(word.word.lower())
        return self.buckets[index]



def main():

    review1 = "Really good institution teachers are very helpful and caring also environment of this college is very attractive Proud to be a part of this college"
    review2 = "Best institution Education level is high"
    review3 = "What so ever I am today is due this technology Temple"
    review4 = "Nice place a big also it provides you good education"
    review5 = "Great institution with opportunities for those who want it"

    word1 = "institution"
    frequency1 = 0
    # We need to find frequency of occurrence of word institution in above 5 reviews

    # 1. Put the data in an effective data structures
    #    > HashTable | Capacity -> number of Words in number of Reviews
    # 2. Implement an Algorithm to calculate frequency
    #    > Whenever a collision will occur we will increment the count
    # 3. Implementation of OOPS with Data Structures is preferable :)
    #    > Word : word, frequency, alphabets

    words1 = review1.split(" ")
    words2 = review2.split(" ")
    words3 = review3.split(" ")
    words4 = review4.split(" ")
    words5 = review5.split(" ")

    capacity = len(words1) + len(words2) + len(words3) + len(words4) + len(words5)

    hTable = HashTable(capacity)

    print(">> Adding Review1 Words in HashTable:", review1)
    for word in words1:
        hTable.put(Word(word))
    print("~~~~~~~~~~~~~~~~")
    print()

    print(">> Adding Review2 Words in HashTable:", review2)
    for word in words2:
        hTable.put(Word(word))
    print("~~~~~~~~~~~~~~~~")
    print()

    print(">> Adding Review3 Words in HashTable:", review3)
    for word in words3:
        hTable.put(Word(word))

    print("~~~~~~~~~~~~~~~~")
    print()

    print(">> Adding Review4 Words in HashTable:", review4)
    for word in words4:
        hTable.put(Word(word))

    print("~~~~~~~~~~~~~~~~")
    print()

    print(">> Adding Review5 Words in HashTable:", review5)
    for word in words5:
        hTable.put(Word(word))

    print("~~~~~~~~~~~~~~~~")
    print()

    hTable.iterate()

    print()

    print("=============================")
    word = hTable.get(Word("institution"))
    print(word)

    word = hTable.get(Word("college"))
    print(word)

    print("=============================")

if __name__ == '__main__':
    main()








