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

        # return for Root Node
        if node.parent is None:
            node.color = 0
            print(">> [Insert] Node's Parent is None for data", data, "Made the Root Node Color as Black")
            return

        # return for left and right child of Root Node
        if node.parent.parent is None:
            return

        # For every other Node, check for violations and fix them
        self.fixInsert(node)

    # Look for violations
    # And Fix Voilations -> either Color Flip Or Rotation
    def fixInsert(self, newNode):

        color = "RED" if newNode.color == 1 else "BLACK"
        print(">> [FIX]: newNode [{}] | [{}]".format(newNode.data, color))

        # Till time, parent of newNode is RED
        while newNode.parent.color == 1:

            # RIGHT CASES : newNode.parent == newNode.parent.parent.right
            if newNode.parent == newNode.parent.parent.right:
                print(">> [FIX]: RIGHT TREE UNBALANCE")
                print(">> [FIX]: newNode.parent [{}] == newNode.parent.parent.right [{}]"
                      .format(newNode.parent.data, newNode.parent.parent.right.data))

                u = newNode.parent.parent.left
                print(">> [FIX]: Uncle u is: [{}] and color is: [{}]".format(u.data, u.color))

                if u.color == 1:
                    print(">> [FIX]: Uncle u {} is RED. Color Flip to Fix Violation".format(u.data))
                    # Change Uncle Color to Black
                    u.color = 0
                    # Change Parent's color as Black
                    newNode.parent.color = 0
                    # GrandParent's Color as Red
                    newNode.parent.parent.color = 1

                    newNode = newNode.parent.parent
                    print(">> [FIXED]: Color Flip Violation Managed".format(u.data))
                else:
                    print(">> [FIX]: Uncle u {} is BLACK. Rotation to Fix Violation".format(u.data))

                    # LEFT CASE IN RIGHT : newNode == newNode.parent.left
                    if newNode == newNode.parent.left:
                        print(">> [FIX]: newNode [{}] == newNode.parent.left [{}]"
                              .format(newNode.data, newNode.parent.left.data))
                        print(">> [FIX]: RIGHT LEFT UNBALANCE")
                        self.rotateRight(newNode)
                        print(">> [FIX]: Flip Colors to BLACK for",
                              newNode.parent.data, "and RED for", newNode.parent.parent.data)

                        newNode.parent.color = 0
                        newNode.parent.parent.color = 1

                    print(">> [FIX] - Ledt Rotate:", newNode.parent.parent.data)
                    self.rotateLeft(newNode.parent.parent)

            # LEFT CASES : newNode.parent != newNode.parent.parent.right
            else:
                print(">> [FIX] - ELSE newNode.parent {} != newNode.parent.parent.right {}".
                      format(newNode.parent.data, newNode.parent.parent.right.data))

                u = newNode.parent.parent.right

                print(">> [FIX]: Uncle u is: [{}] and color is: [{}]".format(u.data, u.color))
                if u.color == 1:
                    print(">> [FIX]: Uncle u {} is RED. Color Flip to Fix Violation".format(u.data))
                    u.color = 0
                    newNode.parent.color = 0
                    newNode.parent.parent.color = 1
                    newNode = newNode.parent.parent
                else:
                    print(">> [FIX]: Uncle u {} is BLACK. Rotation to Fix Violation".format(u.data))
                    if newNode == newNode.parent.right:
                        newNode = newNode.parent
                        print("[FIX] - Black Uncle/Aunt -> Rotate Left -> newNode {} == newNode.parent.right {}"
                              .format(newNode.data, newNode.parent.right.data))
                        self.rotateLeft(newNode)

                    print(">> [FIX]: Flip Colors to BLACK for",
                          newNode.parent.data, "and RED for", newNode.parent.parent.data)
                    newNode.parent.color = 0
                    newNode.parent.parent.color = 1

                    print(">> [FIX] - Right Rotate:", newNode.parent.parent.data)
                    self.rotateRight(newNode.parent.parent)

            # Terminate the Loop
            if newNode == self.root:
                self.root.color = 0
                break


    # Follow AVL Rotation Algorithm
    # But with parent and NIL Node Management :)
    def rotateRight(self, node):
        print(">> [RIGHT ROTATION] for node:", node.data)

    def rotateLeft(self, node):
        print(">> [LEFT ROTATION] for node:", node.data)

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

    # In Red Black Tree as per our implementation, for 1st 3 nodes everything shall work fine
    rbTree.insert(3)    # Black
    rbTree.insert(1)    # Red
    rbTree.insert(5)    # Red

    # Violations starts from 4th Node onwards :)

    # Here we will have 2 consecutive Red Nodes :)
    rbTree.insert(7)

    # Here we will have 2 consecutive Red Nodes Again :)
    rbTree.insert(6)

    rbTree.preOrder(rbTree.root)





if __name__ == '__main__':
    main()