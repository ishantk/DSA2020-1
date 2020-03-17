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
        self.height = 1

    def showNode(self):
        self.object.showProduct()


class AVLTree:

    # size is Property of Class, which is to maintain number of nodes in Tree
    size = 0

    def __init__(self):
        print(">> AVL Tree Object Constructed")

    def insert(self, node, object):

        AVLTree.size += 1

        if node == None:
            node = TreeNode()
            node.object = object

            print("^^^^^^^^^^^^^^^^^^^^")
            print(">> [NODE ADDED] with object:", object)
            object.showProduct()
            print("^^^^^^^^^^^^^^^^^^^^")
            print()

            return node

        # BST Insert Rules:
        # We will only be able to add unique data :)
        if object.pid < node.object.pid:
            node.left = self.insert(node.left, object)
        elif object.pid > node.object.pid:
            node.right = self.insert(node.right, object)
        else:
            return node

        # Since, we have inserted the node height must be added
        # Height for Ancestors must be updated :)
        node.height = self.getMaxHeight(self.height(node.left), self.height(node.right)) + 1
        print(">> NODE HEIGHT IS:", node.height)

        # Check Balance Factor so that we may perform rotation accordingly :)

        balance = self.balanceFactor(node)
        print(">> Balance Factor is:", balance)

        # 4 Cases of UnBalance:
        # Case 1. LEFT LEFT CASE
        if balance > 1 and object.pid < node.left.object.pid:
            print("LEFT LEFT CASE")
            return self.rightRotate(node)

        # Case 2. LEFT RIGHT CASE
        if balance > 1 and object.pid > node.left.object.pid:
            print("LEFT RIGHT CASE")
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 3. RIGHT RIGHT CASE
        if balance < -1 and object.pid > node.right.object.pid:
            print("RIGHT RIGHT CASE")
            return self.leftRotate(node)

        # Case 4. RIGHT LEFT CASE
        if balance < -1 and object.pid < node.right.object.pid:
            print("RIGHT LEFT CASE")
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    # Return the height of the node given as input
    def height(self, node):
        if node != None:
            return node.height
        else:
            return 0

    # Returns Back the Balance Factor to decide upon rotations to further balance the Tree
    def balanceFactor(self, node):
        if node == None:
            return 0

        return self.height(node.left) - self.height(node.right)


    # Utility Function: to know which height is maximum i.e. left or right :)
    def getMaxHeight(self, leftHeight, rightHeight):
        if leftHeight > rightHeight:
            return leftHeight
        else:
            return rightHeight


    def rightRotate(self, y):
        print("RIGHT ROTATION")
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        # Update Height of Affected Nodes:
        y.height = self.getMaxHeight(self.height(y.left), self.height(y.right)) + 1
        x.height = self.getMaxHeight(self.height(x.left), self.height(x.right)) + 1

        return x


    def leftRotate(self, x):
        print("LEFT ROTATION")
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        # Update Height of Affected Nodes:
        y.height = self.getMaxHeight(self.height(x.left), self.height(x.right)) + 1
        x.height = self.getMaxHeight(self.height(y.left), self.height(y.right)) + 1

        return y


    # Please write iterative functions yourself

def main():

    # BST -> Right Skewed Tree
    p1 = Product(101, "AlphaBounce Shoe", 8000)
    p2 = Product(201, "iPhone X", 10000)
    p3 = Product(301, "MacBook", 20000)
    p4 = Product(401, "MacBook", 20000)
    p5 = Product(501, "MacBook", 20000)

    tree = AVLTree()
    rootNode = tree.insert(None, p1)
    tree.insert(rootNode, p2)
    tree.insert(rootNode, p3)
    tree.insert(rootNode, p4)
    tree.insert(rootNode, p5)




if __name__ == '__main__':
    main()