'''
Dungeon Master Problem, BFS search
'''

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['D','C'],
  'D' : ['E'],
  'E' : ['C'],
  'F' : []
}

def bfs(visited, graph, node):

  visited = []
  queue = []

  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, graph, 'A')
