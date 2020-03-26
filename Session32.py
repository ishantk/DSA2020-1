# PS: https://www.cs.usfca.edu/~galles/visualization/BFS.html
#     https://www.cs.usfca.edu/~galles/visualization/DFS.html

class Graph:

    def __init__(self, vertices):
        print("Graph Data Structure Created")
        self.vertices = vertices

        # We will get list of 7 lists where each index will be different reference of list
        self.adjacencyList = [[] for _ in range(vertices)]
        self.visitedNodes = [False for _ in range(vertices)]

        print("Initial Adjacency List of Graph:")
        print(self.adjacencyList)

        # List of VisitedNodes which is as of now False for every vertex :)
        print(self.visitedNodes)


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

    def DFS(self, vertex):

        self.visitedNodes[vertex] = True
        print(vertex, end=" ")

        # print("Iterating:")
        for adjVertex in self.adjacencyList[vertex]:
            # print(adjVertex)
            if not self.visitedNodes[adjVertex]:
                self.DFS(adjVertex)

    """
        DFS(0)
            DFS(1)
                DFS(2)
                    DFS(4)
                        DFS(5)
                  
    """


    def BFS(self, vertex):

        self.visitedNodes[vertex] = True
        queue = []

        # Adding Vertex in the Queue to be processed
        queue.append(vertex)

        while len(queue) != 0:
            v = queue.pop(0)
            print(v, end=" ")

            for adjVertex in self.adjacencyList[v]:
                # print(">> adjVertex:", adjVertex)
                if not self.visitedNodes[adjVertex]:
                    self.visitedNodes[adjVertex] = True
                    queue.append(adjVertex)

            # print("queue is:", queue)

def main():

    # Graph of 7 Vertices from 0 to 6 as in indexed
    graph = Graph(7)

    # False: Edge is not directed i.e. it is bidirectional | UnDirected Graph
    graph.addEdge(0, 1, False)
    graph.addEdge(0, 2, False)
    graph.addEdge(1, 2, False)
    graph.addEdge(1, 3, False)
    graph.addEdge(2, 4, False)
    graph.addEdge(3, 4, False)
    graph.addEdge(4, 5, False)
    graph.addEdge(5, 6, False)

    graph.printAdjacencyList()

    # graph.DFS(0)
    graph.BFS(0)

if __name__ == '__main__':
    main()


# PS: Outputs which we are getting represents MINIMUM SPANNING TREES (MST) with DFS and BFS Algorithm

