class Product:
    # company is attribute which is property of class
    company = "ABC International"

    def __init__(self, pid, price):
        # self is a reference variable which holds hashcode of current object
        # current object : on which you are currently working
        print("self:", self)
        # self.productId and self.price are attributes of Object
        self.productId = pid
        self.price = price


pRef = Product(101, 2000)
pRef.rating = 5.5
print("pRef:", pRef)
print("pRef dictionary:", pRef.__dict__)
print("Product dictionary:", Product.__dict__)

pRef1 = Product(201, 4000)
print("pRef1:", pRef1)