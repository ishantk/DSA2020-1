# HashTable Supports Storage of Only 1 Object at 1 Index :)
class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []

        for i in range(0, capacity):
            self.table.append(None)

    def hashFunction(self, data):
        hashCode = data % self.capacity
        return hashCode


    """
    def put(self, data):
        index = self.hashFunction(data)

        if self.table[index] == None:
            self.table[index] = data
            self.size += 1
        else:
            print(">> We cannot add {}. Please Add Some Other Data :(".format(data))
    """

    def put(self, data):
        index = self.hashFunction(data)

        if self.table[index] == None:
            self.size += 1

        self.table[index] = data
        print(">> Data Added", data)


    def contains(self, data):

        index = self.hashFunction(data)

        if self.table[index] != None and self.table[index] == data:
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

    def remove(self, data):
        index = self.hashFunction(data)
        if self.table[index] == data:
            self.table[index] = None
            print(">> Data Removed :)")
        else:
            print(">> Sorry !! Data Not Found :(")


table1 = HashTable(13)
table2 = HashTable(25)
table3 = HashTable()

table1.put(120)
table1.put(45)
table1.put(66)
table1.put(97)
table1.put(88)

print(table1.table)
print(table1.size)

print("~~~~~~Table Contents~~~~~~~")
table1.iterate()

print(">> is 97 in HashTable? Index:", table1.contains(97))
print(">> is 45 in HashTable? Index:", table1.contains(45))