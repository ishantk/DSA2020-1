class Product:

    def __init__(self, pid, name, price, quantity=1):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print("{} | {} | {}".format(self.pid, self.name, self.price))


class LinkedList:

    size = 0
    total = 0
    items = 0

    def __init__(self):
        print(">> Linked List Object Constructed")
        self.head = None
        self.current = None

    # Circular
    def append(self, object):

        LinkedList.size += 1
        LinkedList.items += object.quantity
        LinkedList.total += (object.price * object.quantity)

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


    def iterateForward(self):

        temp = self.head

        while temp.next != self.head:
            temp.showProduct()
            temp = temp.next

        temp.showProduct()

    def iterateBackward(self):

        temp = self.current

        while temp.previous != self.current:
            temp.showProduct()
            temp = temp.previous

        temp.showProduct()

lRef = LinkedList()
print(">> lRef is:", lRef)
print(">> Dictionary of lRef is:", lRef.__dict__)

print()

# p1 = Product(101, "AlphaBounce Shoe", 8000)
# lRef.append(p1)
lRef.append(Product(101, "AlphaBounce Shoe", 8000))
lRef.append(Product(201, "iPhone X", 70000, 2))
lRef.append(Product(301, "Samsung LED", 50000))
lRef.append(Product(401, "Samsung M10", 1000))
lRef.append(Product(501, "Lays", 20, 3))

lRef.iterateForward()

print("~~~~~~~~~~~~~~")

lRef.iterateBackward()

print("~~~~~~~~~~~~~~")

print(">> LINKED LIST SIZE:", LinkedList.size)
print(">> LINKED LIST ITEMS:", LinkedList.items)
print(">> LINKED LIST TOTAL PRICE:", LinkedList.total)