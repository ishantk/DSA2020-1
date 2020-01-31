class Product:

    def __init__(self, pid, name, price, quantity=1):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print("{} | {} | {}".format(self.pid, self.name, self.price))


class Stack:

    size = 0
    total = 0
    items = 0

    def __init__(self):
        print(">> Linked List Object Constructed")
        self.head = None
        self.current = None

    # Circular
    def push(self, object):

        Stack.size += 1
        Stack.items += object.quantity
        Stack.total += (object.price * object.quantity)

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


    def pop(self):

        Stack.size -= 1
        # manage other variables

        temp = self.current

        self.current = temp.previous
        self.current.next = self.head
        self.head.previous = self.current

        del temp


    def iterate(self):

        temp = self.current

        while temp.previous != self.current:
            temp.showProduct()
            temp = temp.previous

        temp.showProduct()

lRef = Stack()
print(">> lRef is:", lRef)
print(">> Dictionary of lRef is:", lRef.__dict__)

print()

# p1 = Product(101, "AlphaBounce Shoe", 8000)
# lRef.append(p1)
lRef.push(Product(101, "AlphaBounce Shoe", 8000))
lRef.push(Product(201, "iPhone X", 70000, 2))
lRef.push(Product(301, "Samsung LED", 50000))
lRef.push(Product(401, "Samsung M10", 1000))
lRef.push(Product(501, "Lays", 20, 3))

lRef.pop()
lRef.pop()

lRef.push(Product(701, "Macbook", 100000, 1))

lRef.iterate()

print("~~~~~~~~~~~~~~")

print(">> STACK SIZE:", Stack.size)
print(">> STACK ITEMS:", Stack.items)
print(">> STACK TOTAL PRICE:", Stack.total)