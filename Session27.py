"""

    Red Black Trees Properties:
    1. Node is either RED or BLACK
    2. Root is always BLACK
    3. New insertions are always RED
    4. Every Path from root to leaf has the same number of BLACK Nodes
    5. No Path can have 2 consecutive RED Nodes
          if parent is red and any of the child is also red -> Violation
    6. Null Leaves are BLACK


    To maintain above rules, we need to follow an algorithm
    Red Black Tree is a Self Balancing Tree
    ReBalancing itself to maintain above properties

    Checking the Violations and performing necessary actions:
    For any Node
        1. Uncle/Aunt is BLACK
            Rotate Your Tree | AVL Tree Rotation Algo's
            After Rotation, result shall look like this in terms of colors
                    BLACK

                 RED     RED

        2. Uncle/Aunt is RED
            Color Flip

            After Color Flip, result shall look like this in terms of colors
                    RED

                BLACK   BLACK

"""

class TreeNode:

    def __init__(self, data):
        print(">> [RBTreeNode] Constructed With Data:", data)
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        # 3. New insertions are always RED
        self.color = 1

class RedBlackTree:

    def __init__(self):
        print(">> [RedBlackTree] Constructed")

        # Creating a temporary NIL node with data as 0 i.e. nothing
        print(">> [RedBlackTree] Creating a NIL NODE")
        self.NIL = TreeNode(0)

        # Since we are considering our RB Tree's root node is a temporary node. Color is BLACK
        self.NIL.color = 0

        # Make Temporary Null Node as Root Node
        self.root = self.NIL


    def insert(self, data):

        print(">> [Insert] Data:", data)
        # Create TreeNode -> Any Node to be inserted is by default having color value as 1 i.e. RED
        node = TreeNode(data)
        node.left = self.NIL
        node.right = self.NIL

        # Let y be the leaf i.e. NIL
        # And x be the Root of the Tree
        y = None
        x = self.root

        # Check if the tree is empty. i.e. in case x is NIL
        # If so, insert new node as root node and color it black

        # We will iterate and every iteration
        # we will save the reference of parent node in y
        # i.e. After loop terminates, we know the parent node :)
        while x != self.NIL:
            y = x   # To hold the reference of Parent
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y

        # Binary Search Tree Insertion Rules
        if y is None:
            print(">> [Insert] y is None for data", data, "Made the Node as Root")
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            print(">> [Insert] Node's Parent is None for data", data, "Made the Root Node Color as Black")
            return

        if node.parent.parent is None:
            return

        self.fixInsert()

    def fixInsert(self):
        pass

    def rotateRight(self):
        pass

    def rotateLeft(self):
        pass

    def preOrder(self, node):
        if node != None:
            color = "RED" if node.color == 1 else "BLACK"
            print("[{}] | [{}]".format(node.data, color))
            self.preOrder(node.left)
            self.preOrder(node.right)

def main():

    """

             3

         1      5

                    7

                 6


    """

    rbTree = RedBlackTree()
    rbTree.insert(3)
    rbTree.insert(1)
    rbTree.insert(5)
    rbTree.insert(7)
    rbTree.insert(6)
    rbTree.preOrder(rbTree.root)





if __name__ == '__main__':
    main()