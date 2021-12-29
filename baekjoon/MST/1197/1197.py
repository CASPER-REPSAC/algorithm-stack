import sys

sys.stdin = open("D:\내자료\수업\Coding\코테\Python\스터디\\algorithm-stack\\baekjoon\MST\\1197\input.txt","rt")

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
# 간선 정보
edge = []
# 정점, 간선 개수 입력
v, e = map(int, input().split())
# MST를 담을 딕셔너리
vertex = dict()
for i in range(v):
    vertex[i + 1] = i + 1

# A -> B 가중치 C 입력
for _ in range(e):
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

print(vertex)
print(res)