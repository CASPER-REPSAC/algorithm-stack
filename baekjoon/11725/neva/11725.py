from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9)

N = int(stdin.readline())
graph = [{'neighbors': [], 'parent': None} for _ in range(N + 1)]

for _ in range(N - 1):
  l, r = map(int, stdin.readline().strip().split(' '))
  graph[l]['neighbors'].append(r)
  graph[r]['neighbors'].append(l)

def set_parents_using_dfs(now_i):
  for node_i in graph[now_i]['neighbors']:
    if not graph[node_i]['parent']:
      graph[node_i]['parent'] = now_i
      set_parents_using_dfs(node_i)
set_parents_using_dfs(1)

for node in graph[2:]:
  print(node['parent'])
