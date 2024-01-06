# implement shortest path algorithm

graph = {
  'A': [('B', 2), ('C', 6)],
  'B': [('A', 2), ('D', 5)],
  'C': [('A', 6), ('D', 8)],
  'D': [('B', 5), ('C', 8), ('E', 15), ('F', 10)],
  'E': [('D', 15), ('F', 6), ('G', 6)],
  'F': [('D', 10), ('E', 6), ('G', 2)],
  'G': [('E', 6), ('F', 2)]
}

def shortest_path(start, end, graph):
  shortest_path = {
    node: [] for node in graph
  }
  distances = {
    key: float('inf') if key != start else 0
    for key in graph
  }
  unvisited = [
    key for key in graph
  ]

  shortest_path[start] = [start]
  while unvisited:
    # get the near node to check
    current = min(unvisited, key = distances.get)
    # check for adjacent node 
    for node, distance in graph[current]:
      distance_from_start = distances[current] + distance 
      if distance_from_start < distances[node]:
        distances[node] = distance_from_start
        if shortest_path[node] and shortest_path[node][-1] == node:
          shortest_path[node] = shortest_path[current]
        else:
          shortest_path[node].extend(shortest_path[current])
        shortest_path[node].append(node)
    unvisited.remove(current)

  print_shortest_distance(start, end, distances)
  print_shortest_path(end, shortest_path)

def print_shortest_distance(start, end, distances):
  print(f'Shortest distance from {start} to {end} is: {distances[end]}')

def print_shortest_path(end, shortest_path):
  print(f'Shortest path is {"->".join(shortest_path[end])}')
if __name__ == '__main__':
  shortest_path('A', 'C', graph)
