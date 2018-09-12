"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")




def dft(adjList, node_id, visited):
    visited.append(node_id)
    for child_node in adjList[node_id]:
        if child_node not in visited:
            dft(adjList, child_node, visited)




def bft(adjList, node_id):
    frontier = []
    frontier.append(node_id)
    visited = []
    while len(frontier) > 0:
        n = frontier.pop(0)
        if n not in visited:
          print(n)
          visited.append(n)
          for next_node in adjList[n]:
              frontier.append(next_node)








