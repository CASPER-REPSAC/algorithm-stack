import collections
import sys


# 입력
N, M, K, X = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
distance = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)


def bfs(start):
    result = []
    queue = collections.deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        pop = queue.popleft()

        for v in graph[pop]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                distance[v] = distance[pop] + 1
                if distance[v] == K:
                    result.append(v)


    if len(result) == 0:
        print(-1)
    else:
        result.sort()
        for v in result:
            print(v)



bfs(X)


