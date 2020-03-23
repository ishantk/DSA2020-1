"""
    Data Structures
    GRAPHS
"""

# Node in Graph i.e. Vertex in Graph :)
class Node:

    def __init__(self, data):
        self.vertex = data
        self.next = None
        print("[Node] Node Object Constructed with vertex {} and next {}"
              .format(self.vertex, self.next))

    def __str__(self):
        return "{} | {}".format(self.vertex, self.next)

class Graph:

    def __init__(self, vertices=2):
        print("Graph Data Structure Created")
        self.vertices = vertices
        self.nodes = [None] * self.vertices
        print(self.vertices)
        print(self.nodes)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def addEdge(self, vertex1, vertex2):

        print("[ADD EDGE] {} <----> {}".format(vertex1, vertex2))

        node = Node(vertex2)
        node.next = self.nodes[vertex1]
        self.nodes[vertex1] = node

        node = Node(vertex1)
        node.next = self.nodes[vertex2]
        self.nodes[vertex2] = node

        print("[ADD EDGE] self.nodes: ", self.nodes)
        for node in self.nodes:
            print(node)

        print("~~~~~~~~~~~~~~~~~~~~~~~")

    def printGraph(self):

        for i in range(self.vertices):
            print("Adjacency List for Vertex:", i)

            temp = self.nodes[i]
            while temp:
                print(temp.vertex, end="  ")
                temp = temp.next

            print()


def main():

    vertices = 7
    graph = Graph(vertices)

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(2, 4)
    graph.addEdge(3, 4)
    graph.addEdge(4, 5)
    graph.addEdge(5, 6)

    print("===========")

    graph.printGraph()


if __name__ == '__main__':
    main()
