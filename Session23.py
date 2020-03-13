"""

      Balanced Tree

        10
    5       20
  1  7    15  30


     UnBalanced Tree 1
        10              GrandParent

            20          Parent

                30      Child

       Rotate Tree  | Left Rotation
       20

    10   30

    UnBalanced Tree 2

            10

         5

     3

    Rotate Tree  | Right Rotation
       5
    3    10

    UnBalanced Tree 3

        10

            20

        15

        1. Right Rotate

        10

          15

            20

        2. Left Rotate
          15

       10   20

    UnBalanced Tree 4

        10

    12

        15

        1. Left Rotate -> 2. Right Rotate


        1. AVL Trees
        2. Red Black Trees



"""


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
        if node != None:
            self.inOrder(node.left)
            node.object.showProduct()
            self.inOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            node.object.showProduct()

    # Take Input as a Node which is Parent i.e. along which we need to do rotation
    def rotateLeft(self):
        temp = self.rootNode.right
        self.rootNode.right = temp.left
        temp.left = self.rootNode
        self.rootNode = temp


    # Take Input as a Node which is Parent i.e. along which we need to do rotation
    def rotateRight(self):
        temp = self.rootNode.left
        self.rootNode.left = temp.right
        temp.right = self.rootNode
        self.rootNode = temp

    # Need to maintain the height of Tree as well :)
    def isTreeUnBalanced(self):
        pass


"""
tree = Tree()
p1 = Product(101, "AlphaBounce Shoe", 8000)
p2 = Product(201, "iPhone X", 10000)
p3 = Product(301, "MacBook", 20000)

tree.rootNode = tree.add(None, p1)
print(">> ROOT NODE ADDED:", tree.rootNode)

tree.add(tree.rootNode, p2)
tree.add(tree.rootNode, p3)


print("PRE ORDER TRAVERSAL")
tree.preOrder(tree.rootNode)
print()

print("LEFT ROTATION")
tree.rotateLeft()

print("PRE ORDER TRAVERSAL")
tree.preOrder(tree.rootNode)
print()
"""

"""
              8000          gp
            /      \   
           X      10000     p
                /    \           
               y    20000   c
                      
                                    
              8000 10000 20000                                    

            
            Left Rotation
            
            temp -> gp right child                  temp -> 10000
            gp right child -> temp left child       gp right child -> y      
            temp left child -> gp                   temp left child -> 8000
            
            temp -> takes the place of gp           10000 is now the parent
            
            After Rotate Left is applied
            Below Tree and PreOrder should come up :)
            
             10000
          8000  20000
          
          10000 8000 20000  
            

"""

tree = Tree()
p1 = Product(101, "AlphaBounce Shoe", 8000)
p2 = Product(201, "iPhone X", 10000)
p3 = Product(301, "MacBook", 20000)

tree.rootNode = tree.add(None, p3)
print(">> ROOT NODE ADDED:", tree.rootNode)

tree.add(tree.rootNode, p2)
tree.add(tree.rootNode, p1)


print("PRE ORDER TRAVERSAL")
tree.preOrder(tree.rootNode)
print()

print("RIGHT ROTATION")
tree.rotateRight()

print("PRE ORDER TRAVERSAL")
tree.preOrder(tree.rootNode)
print()


"""
              20000          gp
                
        10000                p
        
    8000                     c
                
    PreOrder : 20000 10000 8000
            
            10000
           /    \ 
        8000    20000    

                                            
"""