class Node:

    def __init__(self, data, index, nextNode):
        self.data = data
        self.index = index
        self.nextNode = nextNode

    def showNode(self):
        print("{} | {}".format(self.index, self.data))




class Product:

    def __init__(self, title, rating, isDealOfDay, price, isPrime, nextProduct):
        self.title = title
        self.rating = rating
        self.isDealOfDay = isDealOfDay
        self.price = price
        self.isPrime = isPrime
        self.nextProduct = nextProduct


class LinkedList:

    # Is Property of Class
    head = None
    tail = None
    __size = 0

    def append(self, object):


        node = Node(object, LinkedList.__size, None)

        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        LinkedList.__size += 1

        if LinkedList.head is None:
            LinkedList.head = node
            LinkedList.tail = node
            print(">> [APPEND] LinkedList.head:", LinkedList.head, "[NEXT NODE]:", LinkedList.head.nextNode)
            print(">> [APPEND] LinkedList.tail:", LinkedList.tail)
        else:
            LinkedList.tail.nextNode = node
            print(">> [APPEND] LinkedList.tail.nextNode:",  LinkedList.tail.nextNode)
            LinkedList.tail = node
            print(">> [APPEND] LinkedList.tail:", LinkedList.tail)

        print()

    """
    def appendBeginning(self, object):

        LinkedList.__size += 1
        node = Node(object, None)
        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        temp = LinkedList.head
        LinkedList.head = node
        node.nextNode = temp

        print(">> [APPEND] LinkedList.head:", LinkedList.head, "[NEXT NODE]:", LinkedList.head.nextNode)

        print()
    """

    def updateIndexes(self, node):
        temp = node

        while temp.nextNode is not None:
            temp.index += 1
            temp = temp.nextNode

        temp.index += 1


    def appendBeginning(self, object):


        node = Node(object, 0, None)
        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        LinkedList.__size += 1

        temp = LinkedList.head
        LinkedList.head = node
        node.nextNode = temp

        print(">> [APPEND] LinkedList.head:", LinkedList.head, "[NEXT NODE]:", LinkedList.head.nextNode)

        self.updateIndexes(node.nextNode)

        print()

    def insert(self, index, object):

        LinkedList.__size += 1

        node = Node(object, index, None)
        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        temp = LinkedList.head
        previous = LinkedList.head

        while temp.nextNode is not None:

            if temp.index == index:

                node.nextNode = previous.nextNode
                previous.nextNode = node

                self.updateIndexes(node.nextNode)

                break

            previous = temp
            temp = temp.nextNode

        print()

    def remove(self, object):

        temp = LinkedList.head
        previous = LinkedList.head

        while temp.nextNode is not None:

            if temp.data == object:
                previous.nextNode = temp.nextNode
                del temp

                # Update Indexes

                break

            previous = temp
            temp = temp.nextNode

        print()

    def removeHead(self):

        print()

    def removeTail(self):

        print()

    def removePoistion(self, index):

        print()

    def printList(self):

        temp = LinkedList.head

        while temp.nextNode is not None:
            temp.showNode()
            temp = temp.nextNode

        temp.showNode()

    def size(self):
        return LinkedList.__size


# Lets Create Node Object
# node = Node(85, None)

# Object of LinkedList
lRef = LinkedList()
lRef.append(85)
lRef.append(80)
lRef.append(55)
lRef.append(78)

print(">> Initial List:")
lRef.printList()

print()

lRef.appendBeginning(90)
lRef.appendBeginning(16)
print(">> List with data in Beginning:")
lRef.printList()

print()

print(">> List with data at index 2:")
lRef.insert(2, 77)

lRef.printList()

print(">> Size of Linked List is:", lRef.size())

