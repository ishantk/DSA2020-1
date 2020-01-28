class Node:

    def __init__(self, data, index, nextNode):
        self.data = data
        self.index = index
        self.nextNode = nextNode

    def showNode(self):
        print("{} | {}".format(self.index, self.data))


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

        current = LinkedList.head
        previous = LinkedList.head

        while current.nextNode is not None:

            if current.index == index:

                node.nextNode = previous.nextNode
                previous.nextNode = node

                self.updateIndexes(node.nextNode)

                break

            previous = current
            current = current.nextNode

        print()

    def remove(self, object):

        current = LinkedList.head
        previous = LinkedList.head

        found = False

        while current.nextNode is not None:

            if current.data == object:
                found = True
                previous.nextNode = current.nextNode
                del current

                # Update Indexes
                break

            previous = current
            current = current.nextNode

        # For Last Node
        if found is False:
            if current.data == object:
                previous.nextNode = current.nextNode
                del current

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


    def printNode(self, node):

        if node.nextNode is None:
            node.showNode()
            return

        node.showNode()
        self.printNode(node.nextNode)


    def size(self):
        return LinkedList.__size

    # Recursive Function or Loops along-with it :)
    """
    def insertionSort(self):

        fisrtIdxNode = LinkedList.head.nextNode
        zerothIdxNode = LinkedList.head

        if zerothIdxNode.data > fisrtIdxNode.data:

            LinkedList.head = fisrtIdxNode
            tempIdx = fisrtIdxNode.index

            # Change Indexes
            fisrtIdxNode.index = zerothIdxNode.index
            zerothIdxNode.index = tempIdx

            # Change Nodes
            zerothIdxNode.nextNode = fisrtIdxNode.nextNode
            fisrtIdxNode.nextNode = zerothIdxNode
    """

    def insertionSort(self):

        node = LinkedList.head.nextNode
        current = LinkedList.head


        while node.nextNode != None:
            key = node.data  # 80

            temp = current.nextNode

            while temp.nextNode != node.nextNode:
                temp = temp.nextNode








# Lets Create Node Object
# node = Node(85, None)

# Object of LinkedList
lRef = LinkedList()
lRef.append(85)
lRef.append(80)
lRef.append(77)

print(">> INITIAL LIST: ")
# lRef.printList()
lRef.printNode(LinkedList.head)

print()

print(">> AFTER SORTING LIST: ")
# lRef.insertionSort()
# lRef.printList()

