# Open Hashing
# https://www.cs.usfca.edu/~galles/visualization/OpenHash.html

class Student:

    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def __str__(self):
        return "{} \t {} \t {}".format(self.roll, self.name, self.age)

# HashTable Supports Storage of Only 1 Object at 1 Index :)
class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = []

        for i in range(0, capacity):
            objects = []
            self.buckets.append(objects)

    def hashFunction(self, key):
        hashCode = key % self.capacity
        return hashCode


    def put(self, student):
        key = student.roll+student.age
        index = self.hashFunction(key)

        self.size += 1
        self.buckets[index].append(student)

        print(">> Student Added at index:", index, "Details:", student)


    def contains(self, student):
        key = student.roll + student.age
        pass

    def iterate(self):
        # output will be unordered due to hashing :(
        for i in range(0, len(self.buckets)):
            if len(self.buckets[i]) != 0:
                print(">> Iterating in Bucket:", i)
                for object in self.buckets[i]:
                    print(object)

            print("~~~~~~~~~~~~~~~~~~~~~~~~")

    def remove(self, student):
        key = student.roll + student.age
        pass



s1 = Student(101, "John", 23)
s2 = Student(111, "Jen", 21)
s3 = Student(197, "Jim", 24)
s4 = Student(153, "Jack", 25)
s5 = Student(121, "Joe", 27)

hTable = HashTable()
hTable.put(s1)
hTable.put(s2)
hTable.put(s3)
hTable.put(s4)
hTable.put(s5)

hTable.iterate()