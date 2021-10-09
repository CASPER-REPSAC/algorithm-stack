from collections import deque
import sys

n = int(sys.stdin.readline())

link = {i: [] for i in range(n+1)}

for i in range(n-1):
    a, b = list(map(int, sys.stdin.readline().split()))
    link[a].append(b)
    link[b].append(a)
 
bfs = deque([1])
visit = {i: False for i in range(1, n + 1)}
node = {i: {"parent": [], "child": []} for i in range(1, n + 1)}

while bfs:
    current = bfs.popleft()
    visit[current] = True
    for i in link[current]:
        if not visit[i]:
            node[current]["child"].append(i)
            node[i]["parent"].append(current)
            bfs.append(i)
 
for i in range(2, n + 1):
    print(node[i]["parent"][-1])
