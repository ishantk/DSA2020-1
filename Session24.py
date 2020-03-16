class TreeNode:

    def __init__(self):
        print(">> Tree Node Object Constructed")

        # data as of now is integral. But it can also be an object
        self.data = 0

        self.height = 1
        self.left = None
        self.right = None


class AVLTree:

    # size is Property of Class, which is to maintain number of nodes in Tree
    size = 0

    def __init__(self):
        print(">> AVL Tree Object Constructed")

    def insert(self, node, data):

        AVLTree.size += 1

        if node == None:
            node = TreeNode()
            node.data = data

            print("^^^^^^^^^^^^^^^^^^^^")
            print(">> [NODE ADDED] data is:", data)
            print("^^^^^^^^^^^^^^^^^^^^")
            print()

            return node

        # BST Insert Rules:
        # We will only be able to add unique data :)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
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
        if balance > 1 and data < node.left.data:
            print("LEFT LEFT CASE")
            return self.rightRotate(node)

        # Case 2. LEFT RIGHT CASE
        if balance > 1 and data > node.left.data:
            print("LEFT RIGHT CASE")
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 3. RIGHT RIGHT CASE
        if balance < -1 and data > node.right.data:
            print("RIGHT RIGHT CASE")
            return self.leftRotate(node)

        # Case 4. RIGHT LEFT CASE
        if balance < -1 and data < node.right.data:
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

        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        # Update Height of Affected Nodes:
        y.height = self.getMaxHeight(self.height(y.left), self.height(y.right)) + 1
        x.height = self.getMaxHeight(self.height(x.left), self.height(x.right)) + 1

        return x


    def leftRotate(self, x):

        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        # Update Height of Affected Nodes:
        y.height = self.getMaxHeight(self.height(x.left), self.height(x.right)) + 1
        x.height = self.getMaxHeight(self.height(y.left), self.height(y.right)) + 1

        return y


    def preOrder(self, node):
        if node != None:
            print(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print(node.data)
            self.inOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data)


def main():

    tree = AVLTree()

    rootNode = tree.insert(None, 30)
    tree.insert(rootNode, 5)
    tree.insert(rootNode, 35)
    tree.insert(rootNode, 32)
    tree.insert(rootNode, 40)
    tree.insert(rootNode, 45)


if __name__ == '__main__':
    main()


