# Closed Hashing - Linear Probing
# https://www.cs.usfca.edu/~galles/visualization/ClosedHash.html

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
        self.table = []

        for i in range(0, capacity):
            self.table.append(None)

    def hashFunction(self, key):
        hashCode = key % self.capacity
        return hashCode


    def put(self, student):
        key = student.roll+student.age
        index = self.hashFunction(key)

        if self.table[index] == None:
            self.size += 1

        self.table[index] = student
        print(">> Student Added at index:", index, "Details:", student)


    def contains(self, student):
        key = student.roll + student.age

        index = self.hashFunction(key)

        if self.table[index] != None and self.table[index] == student:
            print(">> Data Found :)")
            return index
        else:
            print(">> Data Not Found :(")
            return -1

    def iterate(self):
        # output will be unordered due to hashing :(
        for data in self.table:
            if data != None:
                print(data)

    def remove(self, student):
        key = student.roll + student.age
        index = self.hashFunction(key)
        if self.table[index] == student:
            self.table[index] = None
            print(">> Data Removed :)")
        else:
            print(">> Sorry !! Data Not Found :(")



s1 = Student(101, "John", 23)
s2 = Student(111, "Jen", 21)
s3 = Student(197, "Jim", 24)
s4 = Student(153, "Jack", 25)
s5 = Student(121, "Joe", 27)

# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)

hTable = HashTable()
hTable.put(s1)
hTable.put(s2)
hTable.put(s3)
hTable.put(s4)
hTable.put(s5)

print(hTable.contains(s4))
print(hTable.contains(s5))

hTable.iterate()