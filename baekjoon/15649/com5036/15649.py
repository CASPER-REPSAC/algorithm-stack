import sys

N, M = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N + 1)]
visit = [False] * N
result = []


def dfs(x):
    if x == M:
        print(*result)
        return

    for i in range(N):
        if visit[i]:
            continue

        visit[i] = True
        result.append(arr[i])
        dfs(x + 1)

        result.pop()
        visit[i] = False

dfs(0)