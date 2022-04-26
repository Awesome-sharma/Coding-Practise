# a --> b , f , d
# b --> a , c , f
# c --> b , e , d
# d --> a , c , e
# e --> d , c , f
# f --> a , b , e


from collections import defaultdict #importing defaultdict

graph = defaultdict(list)


def addNode(graph,u,v):
  graph[u].append(v)


def generate_graph(graph):
  edges = []
  for node in graph:
    for neighbour in graph[node]:
      edges.append((node,neighbour))
  return edges


addNode(graph,"a","b")
addNode(graph,"a","f")
addNode(graph,"a","d")
addNode(graph,"b","a")
addNode(graph,"b","c")
addNode(graph,"b","f")
addNode(graph,"c","b")
addNode(graph,"c","e")
addNode(graph,"c","d")
addNode(graph,"d","a")
addNode(graph,"d","c")
addNode(graph,"d","e")
addNode(graph,"e","d")
addNode(graph,"e","c")
addNode(graph,"e","f")
addNode(graph,"f","a")
addNode(graph,"f","b")
addNode(graph,"f","e")

represent_graph = generate_graph(graph)

print(represent_graph)   #you can also do it like -> print(generate_graph(graph))
