import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

relation = [[0]*(n) for i in range(n)]
infection = [0] * n

for _ in range(m):
    a,b = map(int,input().split())
    a -=1
    b -=1
    relation[a][b] = relation[b][a] = 1

count = []
def dfs(i):
    infection[i]=1
    for j in range(n):
        if relation[i][j] == 1 and infection[j] == 0:
            count.append(j)
            dfs(j)
    return len(count)

print(dfs(0))