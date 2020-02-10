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

    # By Swapping Data In Object
    @staticmethod
    def swapDataInProducts(p1, p2):

        print("Swapping: ", p1.pid, "with", p2.pid)

        # tempPid = p1.pid
        # tempName = p1.name
        # tempPrice = p1.price
        # tempQuantity = p1.quantity
        #
        # p1.pid = p2.pid
        # p1.name = p2.name
        # p1.price = p2.price
        # p1.quantity = p2.quantity
        #
        # p2.pid = tempPid
        # p2.name = tempName
        # p2.price = tempPrice
        # p2.quantity = tempQuantity

        # p1.pid, p2.pid = p2.pid, p1.pid
        # p1.name, p2.name = p2.name, p1.name
        # p1.price, p2.price = p2.price, p1.price
        # p1.quantity, p2.quantity = p2.quantity, p1.quantity

        p1.pid, p1.name, p1.price, p1.quantity, p2.pid, p2.name, p2.price, p2.quantity = p2.pid, p2.name, p2.price, p2.quantity, p1.pid, p1.name, p1.price, p1.quantity


    @staticmethod
    def swapProducts(p1, p2):
        # We must check for head and current which is last
        # p1.next, p1.previous, p2.next, p2.previous = p2.next, p2.previous, p1.next, p1.previous


    def bubbleSort(self):

        iTemp = self.head
        jTemp = self.head

        for i in range(0, LinkedList.size):

            print(">> i is:",i)

            for j in range(0, LinkedList.size - i - 1):
                print(j, end=" ")

                print("[PRICES]", jTemp.price, jTemp.next.price)

                # Swapping with Price
                # if jTemp.price > jTemp.next.price:

                # Swapping with Quantity
                if jTemp.price * jTemp.quantity > jTemp.next.price * jTemp.next.quantity:
                    LinkedList.swapDataInProducts(jTemp, jTemp.next)

                jTemp = jTemp.next

            print()
            jTemp = self.head
            iTemp = iTemp.next


    def iterate(self):
        temp = self.head
        for i in range(0, LinkedList.size):
            temp.showProduct()
            temp = temp.next


lRef = LinkedList()

lRef.append(Product(101, "AlphaBounce Shoe", 8000, 10))
lRef.append(Product(201, "iPhone X", 70000, 1))
lRef.append(Product(301, "Samsung LED", 50000, 2))
lRef.append(Product(401, "Samsung M10", 1000, 12))
lRef.append(Product(501, "Lays", 20, 5))

lRef.bubbleSort()
lRef.iterate()
