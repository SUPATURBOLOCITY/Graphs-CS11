"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vert):
        self.vertices[vert] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")


def dft(adjList, node_id):
    print(node_id)
    for n in adjList[node_id]:
        dft(adjList, n)

def bft(adjList, node_id):
    frontier = []
    frontier.append(node_id)
    while len(frontier) > 0:
        n = frontier.pop(0)
        print(n)
        for next_node in adjList[n]:
            frontier.append(next_node)


# dft(graph.vertices, 0)
# bft(graph.vertices, 0)

