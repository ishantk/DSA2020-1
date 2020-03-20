"""

    Red Black Tree Properties:
    1. Color Property:
        Every Node is Colored. Either Red or Black
    2. Root Property:
        The root of Tree is always Black
    3. Leaf Property:
        nil nodes i.e. the leaves are always Black
    4. Red Property:
        If a red node has children, they are always BLack
    5. Depth Property:
        For Each Node, any simple path from this node
        to its descendant shall have the same Black Nodes

    In a RedBlack Tree we insert the data by following the Rules of BST
    But, attributes of Node and insertion process shall be different

    Attributes of Node in RB Tree
        color, data, left, right, parent

        color -> 0 is BLACK | 1 is RED


"""

class TreeNode:

    def __init__(self, data):

        print(">> RB Tree [Node] Object Constructed")

        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:

    def __init__(self):
        print(">> Red Black [Tree] Object Constructed")

        # Creating a temporary null node with data as 0
        print(">> Red Black [Tree] Creating a TNULL NODE")
        self.TNULL = TreeNode(0)

        # Since we are considering our RB Tree's root node is a temporary node. Color is BLACK
        self.TNULL.color = 0

        # Make Temporary Null Node as Root Node
        self.root = self.TNULL


    def insert(self, data):
        print(">> Inserting:", data)
        # Create TreeNode -> Any Node to be inserted is by default having color value as 1 i.e. RED
        node = TreeNode(data)
        node.left = self.TNULL
        node.right = self.TNULL

        # Let y be the leaf i.e. NIL
        # And x be the Root of the Tree
        y = None
        x = self.root

        # Check if the tree is empty. i.e. in case x is NIL
        # If so, insert new node as root node and color it black

        # We will iterate and every iteration we will save the reference of previous node in y
        while x != self.TNULL:
            y = x   # To hold the reference of Parent
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y

        if y is None:
            print(">> y is None for data", data, "Made the Node as Root")
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            print(">> Node's Parent is None for data", data, "Made the Root Node Color as Black")
            return

        if node.parent.parent is None:
            return

    # Violations of RB Tree shall be looked by this function
    # Particularly either rotation or color flip will be done in below function:
    def fixInsert(self):
        pass

def main():
    rbTree = RedBlackTree()
    rbTree.insert(50)
    rbTree.insert(40)
    rbTree.insert(70)
    rbTree.insert(60)
    rbTree.insert(80)
    rbTree.insert(55)


if __name__ == '__main__':
    main()