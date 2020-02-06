# PS: https://www.cs.usfca.edu/~galles/visualization/BST.html

class Product:

    def __init__(self, pid, name, price, quantity=1):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print("{} | {} | {}".format(self.pid, self.name, self.price))


class TreeNode:

    def __init__(self):
        self.object = None
        self.left = None
        self.right = None

    def showNode(self):
        self.object.showProduct()

# Uniqueness| Key is Unique
class Tree:

    size = 0

    def __init__(self):
        print(">> Tree Object Constructed")
        self.rootNode = None

    def add(self, node, object):

        if node == None:

            node = TreeNode()
            node.object = object

            print("^^^^^^^^^^^^^^^^^^^^")
            print(">> [NODE ADDED]")
            node.showNode()
            print("^^^^^^^^^^^^^^^^^^^^")
            print()

            return node

        if object.price < node.object.price:
            node.left = self.add(node.left, object)
        else:
            node.right = self.add(node.right, object)

        return node

    def preOrder(self, node):

        if node != None:
            node.object.showProduct()
            self.preOrder(node.left)
            self.preOrder(node.right)


    def inOrder(self, node):
        pass

    def postOrder(self, node):
        pass

    def minimumNode(self, node):
        pass

    def maximumNode(self, node):
        pass


tree = Tree()
tree.rootNode = tree.add(None, Product(101, "AlphaBounce Shoe", 8000))
print(">> ROOT NODE ADDED:", tree.rootNode)

tree.add(tree.rootNode, Product(201, "iPhone X", 70000, 2))
tree.add(tree.rootNode, Product(301, "LED", 5000))
tree.add(tree.rootNode, Product(401, "Samsung M10", 1000))
tree.add(tree.rootNode, Product(501, "MacBook", 100000, 3))
tree.add(tree.rootNode, Product(601, "Samsung M40", 9000, 1))

print("PRE ORDER TRAVERSAL")
tree.preOrder(tree.rootNode)

"""
              8000
             /    \
      5000             70000
     /                /     \
  1000           9000        100000
            

 Pr O: 8000 - 5000 - 1000 - 70000 - 9000 - 100000
 In O: 1000 - 5000 - 8000 - 9000 - 70000 - 100000
 Po O: 1000 - 5000 - 9000 - 100000 - 70000 - 8000

"""


