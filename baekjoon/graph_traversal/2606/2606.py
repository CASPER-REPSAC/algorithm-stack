import sys
sys.stdin = open("algorithm-stack\\baekjoon\graph_traversal\\2606\input.txt")
input = sys.stdin.readline

dic = dict()

for i in range(int(input())):
    dic[i+1] = set()
for j in range(int(input())):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)

print(dic)
visited = []
dfs(1, dic)
print(visited)
print(len(visited) - 1)