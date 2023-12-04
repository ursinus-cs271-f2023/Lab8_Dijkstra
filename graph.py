from heap import MinPQ

UNTOUCHED = 0
FRONTIER = 1
VISITED = 2

class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbs = set([]) # Stores (weight, vertex label) tuples
        self.state = UNTOUCHED
        self.prev = None
    
    def __repr__(self):
        return "{}".format(self.label)

class Graph:
    def __init__(self):
        # Key: Vertex label to look up
        # Value: object encapsulating information about that vertex
        self.vertices = {}

    def add_vertex(self, u):
        self.vertices[u] = Vertex(u)
    
    def add_edge(self, u, v, w):
        """
        Add a weighted edge between two vertices

        Parameters
        ----------
        u: hashable
            Hashable identifier of first vertex (usually int or string)
        v: hashable
            Hashable identifier of second vertex (usually int or string)
        w: float
            Weight of edge
        """
        self.vertices[u].neighbs.add((w, v))
        self.vertices[v].neighbs.add((w, u))
    
    def explore(self, start):
        """
        Given V vertices and E edges in the graph
        
        Perform Dijkstra's algorithm to find the lengths of the shortest 
        paths from "start" to all other vertices

        Parameters
        ----------
        start: hashable
            Label of vertex at which to start the search
        
        Returns
        -------
        dictionary: label->distance
            Distance of all vertices from the start
        """
        for v in self.vertices.values():
            v.state = UNTOUCHED
        frontier = MinPQ()
        frontier.push([0, start])
        distances = {} ## TODO: Fill this in
        # Each vertex passes through the frontier exactly once
        while len(frontier) > 0: # O(V) iterations
            ## TODO: Take off the node at the front and record its distance
            [d, vertex] = frontier.pop()
            distances[vertex] = d
            self.vertices[vertex].state = VISITED

            # Look at each neighbor of v.  Add its weight to the distance
            # to get d'
            # a) If it's not on the queue and it hasn't been visited, 
            # add the neighbor with priority d'
            # b) If it's already on the queue and d' is less than its priority, 
            # update the priority
            # Otherwise, if it's already been visited, do nothing
            for (w, n) in self.vertices[vertex].neighbs:
                if self.vertices[n].state == UNTOUCHED:
                    frontier.push([d+w, n])
                    self.vertices[n].state = FRONTIER
                    self.vertices[n].prev = vertex
                elif self.vertices[n].state == FRONTIER:
                    if frontier.get_priority(n) > d+w:
                        frontier.update_priority(n, d+w)
                        self.vertices[n].prev = vertex
                    

        
        return distances
    
    def backtrace(self, x):
        path = [x]
        while self.vertices[path[-1]].prev is not None:
            path.append(self.vertices[path[-1]].prev)
        return path