from shlex import quote


class Product:

    def __init__(self, pid, name, price, quantity=1):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print("{} | {} | {}".format(self.pid, self.name, self.price))


class Queue:

    size = 0
    total = 0
    items = 0

    def __init__(self):
        print(">> QUEUE Object Constructed")
        self.head = None
        self.current = None

    # Circular
    # Add the data in the end
    def add(self, object):

        Queue.size += 1
        Queue.items += object.quantity
        Queue.total += (object.price * object.quantity)

        print(">> object is:", object)
        object.next = None
        object.previous = None
        print(">> object dictionary is:", object.__dict__)
        print()

        if self.head == None:
            self.head = object
            self.current = object
            print("---------------------------------")
            print(">> object added at head:", object)
            print("---------------------------------")
        else:
            self.current.next = object
            object.previous = self.current

            self.head.previous = object

            self.current = object
            self.current.next = self.head

        print(">> NEXT {} PREVIOUS {}".format(object.next, object.previous))


    # Remove Head of Queue
    # FIFO
    def poll(self):

        Queue.size -= 1
        # manage other variables

        print(">> Deleting Node:")
        self.head.showProduct()
        print("~~~~~~~~~~~~~~~~~")

        self.head = self.head.next
        self.head.previous = self.current
        self.current.next = self.head

        # Here we will have 1 node i.e. previous head which will not be pointed by anyone,
        # and shall be deleted automatically


    def iterate(self):

        temp = self.head

        while temp.next != self.head:
            temp.showProduct()
            temp = temp.next

        temp.showProduct()


    def peek(self):
        print(">> Head Node:")
        self.head.showProduct()
        print("~~~~~~~~~~~~~~~~~")


queue = Queue()
print(">> queue is:", queue)
print(">> Dictionary of queue is:", queue.__dict__)

print()

# p1 = Product(101, "AlphaBounce Shoe", 8000)
# lRef.append(p1)
queue.add(Product(101, "AlphaBounce Shoe", 8000))
queue.add(Product(201, "iPhone X", 70000, 2))
queue.add(Product(301, "Samsung LED", 50000))
queue.add(Product(401, "Samsung M10", 1000))
queue.add(Product(501, "Lays", 20, 3))

queue.poll()
queue.poll()

queue.add(Product(601, "Macbook", 100000, 1))

queue.iterate()

print("~~~~~~~~~~~~~~")

print(">> QUEUE SIZE:", Queue.size)
print(">> QUEUE ITEMS:", Queue.items)
print(">> QUEUE TOTAL PRICE:", Queue.total)

print("~~~~~~~~~~~~~~")
queue.peek()


# HW Singly LinkedList -> Implement Stack and Queue
# Implement Search and Sort | Circluar Linked List :)
# CW Use Inheritance Technique -> LinkedList is Parent | Stack and Queue are Children


"""
HAS-A
class Customer:

    def __init__(self, name, phone, email, address):
        pass

class Address:

    def __init__(self, adrsLine, city, state, zipCode):
        pass

# aRef = Address(....)
# cRef = Customer(..., aRef)
"""

"""
IS-A
class LinkedList
    pass
    
class Stack(LinkedList):
    pass    

class Queue(LinkedList):
    pass
    
# ref = LinkedList()
# ref = Stack()
# ref = Queue()    

"""
