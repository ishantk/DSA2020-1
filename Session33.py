class Edge:

    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def getEdgeDetails(self):
        return "Edge: {} <---{}---> {}".format(self.vertex1, self.weight, self.vertex2)


class Graph:

    def __init__(self):
        self.vertices = dict()

    # UnDirected Graph, we will add both users to each others adjacency list
    # For Directed Graph we must set isDirected to True
    def addEdge(self, edge, isDirected=False):

        if edge.vertex1 not in self.vertices:
            self.vertices[edge.vertex1] = []

        if edge.vertex2 not in self.vertices:
            self.vertices[edge.vertex2] = []

        # Maintain Adjacency List
        # Maintain the data in List as Tuple, where we have adjacent vertex and weight
        self.vertices[edge.vertex1].append((edge.vertex2, edge.weight))

        if not isDirected:
            self.vertices[edge.vertex2].append((edge.vertex1, edge.weight))


    def printGraph(self):
        print("Number of Vertices in Graph:", len(self.vertices))

        keys = self.vertices.keys()

        # Printing Adjacency List
        for key in keys:
            # print(">> Adjacency List for Vertex:", key)
            print(key, ":", end=" ")
            print(self.vertices[key], end=" ")
            print()
            print("----------------------------------")

        # Your Code to Print Adjacency Matrix

def main():

    """
    # UnDirected Graph
    edge0 = Edge(0, 1, 4)
    edge1 = Edge(0, 2, 4)
    edge2 = Edge(0, 3, 6)
    edge3 = Edge(0, 4, 6)
    edge4 = Edge(1, 2, 2)
    edge5 = Edge(2, 3, 8)
    edge6 = Edge(3, 4, 9)

    # edges = [Edge(0, 1, 4), Edge(0, 2, 4)]

    edges = [edge0, edge1, edge2, edge3, edge4, edge5, edge6]

    for edge in edges:
        print(edge.getEdgeDetails())


    graph = Graph()
    graph.printGraph()

    for edge in edges:
        graph.addEdge(edge)

    graph.printGraph()
    """

    # Directed Graph
    edge0 = Edge(0, 1, 99)
    edge1 = Edge(0, 2, 50)
    edge2 = Edge(1, 2, 50)
    edge3 = Edge(1, 3, 50)
    edge4 = Edge(1, 4, 50)
    edge5 = Edge(2, 3, 99)
    edge6 = Edge(3, 4, 75)

    edges = [edge0, edge1, edge2, edge3, edge4, edge5, edge6]

    for edge in edges:
        print(edge.getEdgeDetails())

    graph = Graph()
    graph.printGraph()

    for edge in edges:
        # We pass True for Directed Graph
        graph.addEdge(edge, True)

    graph.printGraph()


if __name__ == '__main__':
    main()