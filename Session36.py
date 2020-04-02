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
        self.vertices = {}

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
            self.vertices[edge.vertex1] = []

        if edge.vertex2 not in self.vertices:
            self.vertices[edge.vertex2] = []

        # Maintain Adjacency List
        # Maintain the data in List of Vertices
        self.vertices[edge.vertex1].append(edge.vertex2)

        if not isDirected:
            self.vertices[edge.vertex2].append(edge.vertex1)

    def removeEdge(self, edge, isDirected=False):

        self.edges.remove(edge)

        self.vertices[edge.vertex1].remove(edge.vertex2)

        if not isDirected:
            self.vertices[edge.vertex2].remove(edge.vertex1)


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

    def printEdges(self):
        for edge in self.edges:
            print(edge.getEdgeDetails())


    # For Kruskals to run we need to have sorted edges
    def sortEdges(self):
        # Creating a New List edgeList where we are copying the data from self.edges
        edgeList = self.edges[:]

        from operator import attrgetter
        edgeList.sort(key=attrgetter('weight'), reverse=False)  # reverse=False -> Ascending Order
        return edgeList

    # Refine this algorithm below:
    # check for any cycle made by adding edge to Graph (Consider and think of all the use cases :)
    def kruskals(self):

        # Lets create a new Graph Object : Minimum Spanning Tree
        mst = Graph()

        edgeList = self.sortEdges()
        for edge in edgeList:
            print(">> Adding Edge to MST: ", edge.getEdgeDetails())

            mst.addEdge(edge)

            # Create Set of Adjacent Vertices
            set1 = set(mst.vertices[edge.vertex1])
            set2 = set(mst.vertices[edge.vertex2])

            set3 = set1.intersection(set2)

            print("----------------------")
            print(set1, set2)
            print(set3)


            if len(set3) != 0:
                mst.removeEdge(edge)
                print(">> Removing Edge from MST: ", edge.getEdgeDetails())
                print("----------------------")

            print()


        return mst

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

    print("====Running Kruskals to get MST====")

    mst = graph.kruskals()

    print("==MST Details==")
    mst.printGraph()
    mst.printEdges()


if __name__ == '__main__':
    main()
