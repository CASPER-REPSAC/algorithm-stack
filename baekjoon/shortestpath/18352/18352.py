import sys
from collections import deque

sys.stdin = open("baekjoon\shortestpath\\18352\input.txt")
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

dic = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
visited[x] = 0

for j in range(m):
    a,b = map(int, input().split())
    dic[a].append(b)

def path(start):
    queue = deque([start])
    while queue:
        cur = int(queue.popleft())
        for i in dic[cur]:
            if visited[i] == -1:
                visited[i] = visited[cur] + 1
                queue.append(i)

path(x)
ans = []
for i in range(n + 1):
    if visited[i] == k:
        ans.append(i)

if ans:
    for i in ans:
        print(i)
else:
    print(-1)