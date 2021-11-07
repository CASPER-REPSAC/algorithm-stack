import sys
from collections import deque


def bfs(start_v):
    visit = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(n + 1):
            if graph[v][i] == 1 and i not in visit:
                queue.append(i)
                visit.append(i)


def dfs(v):
    visit_dfs[v] = 1
    print(v, end=' ')

    for i in range(n + 1):
        if graph[v][i] == 1 and i not in visit_dfs:
            dfs(i)


n, m, start_v = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    m1, m2 = map(int, sys.stdin.readline().split())
    graph[m1][m2] = graph[m2][m1] = 1

visit_dfs = {}
dfs(start_v)
print()
bfs(start_v)
