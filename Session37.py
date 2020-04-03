import sys

class Edge:

    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def getEdgeDetails(self):
        return "Edge: {} <---{}---> {}".format(self.vertex1, self.weight, self.vertex2)


class Graph:

    def __init__(self, edges=None):
        # Dictionary Of Vertices in Graph
        self.adjList = {}
        self.vertices = {}
        self.visitedVertices = []
        self.unVisitedVertices = []

        # Maintain edges in the Graph Object
        self.edges = []

        if edges is not None:
            for edge in edges:
                self.addEdge(edge)



    # UnDirected Graph, we will add both users to each others adjacency list
    # For Directed Graph we must set isDirected to True
    def addEdge(self, edge, isDirected=False):

        self.edges.append(edge)

        if edge.vertex1 not in self.vertices:
            self.adjList[edge.vertex1] = []
            self.vertices[edge.vertex1] = [None, sys.maxsize]
            self.unVisitedVertices.append(edge.vertex1)

        if edge.vertex2 not in self.vertices:
            self.adjList[edge.vertex2] = []
            self.vertices[edge.vertex2] = [None, sys.maxsize]
            self.unVisitedVertices.append(edge.vertex2)

        # Maintain Adjacency List
        # Maintain the data in List of Vertices
        self.adjList[edge.vertex1].append(edge.vertex2)

        if not isDirected:
            self.adjList[edge.vertex2].append(edge.vertex1)


    def printGraph(self):
        print("Number of Vertices in Graph:", len(self.adjList))

        keys = self.adjList.keys()

        # Printing Adjacency List
        for key in keys:
            # print(">> Adjacency List for Vertex:", key)
            print(key, ":", end=" ")
            print(self.adjList[key], end=" ")
            print()
            print("----------------------------------")

    def printEdges(self):
        for edge in self.edges:
            print(edge.getEdgeDetails())

    def printVertices(self):
        print("Number of Vertices in Graph:", len(self.vertices))
        keys = self.vertices.keys()
        print("{}  |  {}  |  {} ".format("Vertex", "Parent", "Weight"))
        for key in keys:
            print("{}  |  {}  |  {} ".format(key, self.vertices[key][0], self.vertices[key][1]))

        print(">> Visited Vertices:", self.visitedVertices)
        print(">> UnVisited Vertices:", self.unVisitedVertices)

    # Implement
    def prims(self, sourceVertex):
        pass

def main():

    # UnDirected Graph
    edge0 = Edge(0, 1, 9)
    edge1 = Edge(0, 2, 75)
    edge2 = Edge(1, 2, 95)
    edge3 = Edge(1, 3, 19)
    edge4 = Edge(1, 4, 42)
    edge5 = Edge(2, 3, 51)
    edge6 = Edge(3, 4, 31)

    edges = [edge0, edge1, edge2, edge3, edge4, edge5, edge6]

    graph = Graph(edges)

    graph.printGraph()
    graph.printEdges()
    graph.printVertices()

    # print("====Running Prims to get MST====")
    # mst = graph.prims(0)


if __name__ == '__main__':
    main()
