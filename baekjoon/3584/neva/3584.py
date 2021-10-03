from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9)

def get_stem(node_i):
  way = [node_i]
  if graph[node_i]['parent']:
    way += get_stem(graph[node_i]['parent'])
  return way

for _ in range(int(stdin.readline())):
  N = int(stdin.readline())
  graph = [{'parent': None} for _ in range(N + 1)]
  for _ in range(N - 1):
    A, B = [*map(int, stdin.readline().strip().split())]
    graph[B]['parent'] = A
  node_a, node_b = [*map(int, stdin.readline().strip().split())]
  node_a_stem, node_b_stem = get_stem(node_a), get_stem(node_b)

  same_stem = []
  for node_a_point, node_b_point in zip(node_a_stem[::-1], node_b_stem[::-1]):
    if node_a_point != node_b_point:
      break
    else:
      same_stem.append(node_a_point)
  print(same_stem[-1])
