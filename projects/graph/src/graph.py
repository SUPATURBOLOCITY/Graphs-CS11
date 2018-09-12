import random

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3)
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id / 10 * (self.id // 3)
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            colorString = "#"
            for i in range(0, 3):
                colorString += hexValues[random.randint(0,len(hexValues) - 1)]
            # Algorithm for bright colors
            # colorArray = ["F"]
            # for i in range(0, 2):
            #     colorArray.append(hexValues[random.randint(0,len(hexValues) - 1)])
            # random.shuffle(colorArray)
            # colorString = "#" + "".join(colorArray)
            # print(colorString)
            self.color = colorString


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")




# def dft(adjList, node_id, visited):
#     visited.append(node_id)
#     for child_node in adjList[node_id]:
#         if child_node not in visited:
#             dft(adjList, child_node, visited)


# def bft(adjList, node_id):
#     frontier = []
#     frontier.append(node_id)
#     visited = []
#     while len(frontier) > 0:
#         n = frontier.pop(0)
#         if n not in visited:
#           print(n)
#           visited.append(n)
#           for next_node in adjList[n]:
#               frontier.append(next_node)


