# Directed/Undirected Weighted Graph
# Use Case : Google Map

# Location or Place in Map
# For our Graph Data Structure, Location is kind of Node/Vertex
class Location:

    # A location can have several attributes as in whatever needed
    def __init__(self, latitude, longitude, adrsLine):
        self.latitude = latitude
        self.longitude = longitude
        self.adrsLine = adrsLine

    def getLocationDetails(self):
        return "{} [{},{}]".format(self.adrsLine, self.latitude, self.longitude)

# For our Graph Data Structure, Path is kind of Edge (Location1, Location2, weight)

class Path:

    def __init__(self, location1, location2, distance):
        self.location1 = location1
        self.location2 = location2
        self.distance = distance
        self.traffic = 1        # 1 as free flow, 2 as moderate, 3 as jammed

    def getPathDetails(self):
        return "{} <----- {} -----> {}".format(self.location1.adrsLine, self.distance, self.location2.adrsLine)

# Directed/Undirected Weighted Graph
class GoogleMap:

    def __init__(self):
        self.locations = dict()

    # UnDirected Graph, we will add both users to each others adjacency list
    # For Directed Graph we must set isDirected to True
    def addPath(self, path, isDirected=False):

        if path.location1 not in self.locations:
            self.locations[path.location1] = []

        if path.location2 not in self.locations:
            self.locations[path.location2] = []

        # Maintain Adjacency List
        # Maintain the data in List as Tuple, where we have adjacent vertex and weight
        self.locations[path.location1].append(path.location2)

        if not isDirected:
            self.locations[path.location2].append(path.location1)

    def printGoogleMap(self):
        print("Number of Locations in Graph:", len(self.locations))

        keys = self.locations.keys()

        # Printing Adjacency List
        for key in keys:
            print(key.getLocationDetails())

            print("Adjacent Locations:")

            for location in self.locations[key]:
                print(location.getLocationDetails())

            print("----------------------------------")
            print()


def main():

    location1 = Location(75.234, 72.123, "1. Redoowd Shores")
    location2 = Location(85.234, 82.123, "2. Country Homes")
    location3 = Location(121.234,112.123, "3. Pristine Magnum")
    location4 = Location(79.324, 81.123, "4. Bay Side")
    location5 = Location(75.234, 77.123, "5. Castle Woods")

    path1 = Path(location1, location2, 10)
    path2 = Path(location1, location3, 12)
    path3 = Path(location1, location4, 12)
    path4 = Path(location2, location3, 16)
    path5 = Path(location3, location4, 13)
    path6 = Path(location4, location5, 19)

    paths = [path1, path2, path3, path4, path5, path6]

    for path in paths:
        print(path.getPathDetails())

    graph = GoogleMap()
    graph.printGoogleMap()

    for path in paths:
        # UnDirected Graph
        # graph.addPath(path)

        # We pass True for Directed Graph
        graph.addPath(path, True)

    print()
    print(">> Printing Google Map with Adacent Locations:")
    graph.printGoogleMap()


if __name__ == '__main__':
    main()