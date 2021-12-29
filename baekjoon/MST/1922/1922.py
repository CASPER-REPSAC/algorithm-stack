import sys

sys.stdin = open("algorithm-stack\\baekjoon\MST\\1922\input.txt","rt")

# 사이클이 발생하는지 확인
def find_parent(vertex, x):
    if vertex[x] != x:
        vertex[x] = find_parent(vertex, vertex[x])
    return vertex[x]

# 간선 연결
def union_parent(vertex, a, b):
    a = find_parent(vertex, a)
    b = find_parent(vertex, b)
    if a < b:
        vertex[b] = a
    else:
        vertex[a] = b

res = 0
# 간선 리스트
edge = []
# 컴퓨터 수(정점) 입력
N = int(sys.stdin.readline())
# 선의 수(간선) 입력
M = int(sys.stdin.readline())
# MST 트리
vertex = dict()
for i in range(N):
    vertex[i + 1] = i + 1

# A -> B 가중치 C 입력
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append((a,b,c))

# Kruskal MST
# 가중치 기준 오름차순 정렬
edge = sorted(edge, key=lambda weight: weight[2])

# MST 생성
for edge in edge:
    a, b, c = edge
    if find_parent(vertex, a) != find_parent(vertex, b):
        union_parent(vertex, a, b)
        res += c

print(res)