import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)

result = []


def dfs(x):
    if x == M:
        print(*result)
        return

    for i in range(N):
        try:
            if result[-1] > arr[i]:
                continue
        except IndexError:
            pass

        result.append(arr[i])
        dfs(x + 1)
        result.pop()


dfs(0)
