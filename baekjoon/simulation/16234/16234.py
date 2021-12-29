import sys
from collections import deque

sys.stdin = open("baekjoon\simulation\\16234\input.txt")
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

answer = 0
people = 0
visited = set()
flag = False
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def sol(x, y):
    global flag, people
    queue = deque()
    queue.append((x, y))
    union.append((x, y))

    while queue:
        q = queue.popleft()
        for i in range(4):
            nx = q[0] + dx[i]
            ny = q[1] + dy[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if (nx, ny) not in visited:
                    if L <= abs(A[q[0]][q[1]] - A[nx][ny]) <= R:
                        flag = True
                        visited.add((nx, ny))
                        people += A[nx][ny]
                        queue.append((nx, ny))
                        union.append((nx, ny))


while True:
    flag = False
    visited.clear()
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited:
                union = deque()
                people = A[i][j]
                visited.add((i, j))
                sol(i, j)
                if len(union) > 1:
                    avg = people // len(union)
                    while union:
                        a = union.popleft()
                        A[a[0]][a[1]] = avg
    
    if not flag:
        break
    answer += 1
    
print(answer)