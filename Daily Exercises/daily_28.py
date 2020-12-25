'''
Disclosure: This is not my solution, I am saving it for notes.

You are given a 2-d matrix where each cell consists of either /, \, or an empty space. Write an algorithm that determines into how many regions the slashes divide the space.

For example, suppose the input for a three-by-six grid is the following:

\    /
 \  /
  \/
Considering the edges of the matrix as boundaries, this divides the grid into three triangles, so you should return 3.
'''

from collections import defaultdict

def create_graph(matrix):
    graph = defaultdict(list)

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] == '/':
                graph[(i, j + 1)].append((i + 1, j))
                graph[(i + 1, j)].append((i, j + 1))
            elif matrix[i][j] == '\\':
                graph[(i, j)].append((i + 1, j + 1))
                graph[(i + 1, j + 1)].append((i, j))

    return graph

def traverse(start, graph, walls, walls_hit, visited, regions):
    visited.add(start)

    neighbors = graph[start]
    for neighbor in neighbors:
        graph[neighbor].remove(start)

    for neighbor in neighbors:
        if neighbor in visited:
            regions += 1
        else:
            if neighbor in walls:
                walls_hit += 1
                if walls_hit > 1:
                    regions += 1
            regions, walls_hit = traverse(neighbor, graph, walls, walls_hit, visited, regions)

    return regions, walls_hit

from itertools import product

def get_regions(matrix):
    graph = create_graph(matrix)
    vertices = list(graph.keys())

    m, n = len(matrix), len(matrix[0])
    walls = set(list(product((0, m), range(n + 1))) + list(product(range(1, m), (0, n))))

    regions = 1
    visited = set()

    while vertices:
        start = vertices[0]
        walls_hit = 1 if start in walls else 0
        regions, _ = traverse(start, graph, walls, walls_hit, visited, regions)
        vertices = [v for v in vertices if v not in visited]

    return regions
