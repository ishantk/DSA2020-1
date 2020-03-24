class Graph:

    def __init__(self, vertices):
        print("Graph Data Structure Created")
        self.vertices = vertices

        # We got list of 7 lists where each index was the same reference of list
        # self.adjacencyList = [[]] * self.vertices

        # We will get list of 7 lists where each index will be different reference of list
        self.adjacencyList = [[] for _ in range(vertices)]
        print("Initial Adjacency List of Graph:")
        print(self.adjacencyList)


    def addEdge(self, vertex1, vertex2, isDirected):

        print("EDGE ADDED {} <-----> {}".format(vertex1, vertex2))

        self.adjacencyList[vertex1].append(vertex2)

        # In case of Undirected i.e. Bidirectional graph
        if isDirected == False:
            self.adjacencyList[vertex2].append(vertex1)

    def printAdjacencyList(self):
        # for adjList in self.adjacencyList:
        #     print(adjList)

        for i in range(len(self.adjacencyList)):
            print("{}  |  {}".format(i, self.adjacencyList[i]))


def main():

    # Graph of 7 Vertices from 0 to 6 as in indexed
    # graph = Graph(7)

    # False: Edge is not directed i.e. it is bidirectional | UnDirected Graph
    """
    graph.addEdge(0, 1, False)
    graph.addEdge(0, 2, False)
    graph.addEdge(1, 2, False)
    graph.addEdge(1, 3, False)
    graph.addEdge(2, 4, False)
    graph.addEdge(3, 4, False)
    graph.addEdge(4, 5, False)
    graph.addEdge(5, 6, False)
    """

    graph = Graph(3)

    # True: Edge is directed i.e. it is directional | Directed Graph
    graph.addEdge(0, 1, True)
    graph.addEdge(1, 2, True)
    graph.addEdge(2, 0, True)


    graph.printAdjacencyList()


if __name__ == '__main__':
    main()