import collections
import sys


def union(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def get_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]


def is_same_parent(a, b):
    if get_parent(a) == get_parent(b):
        return True
    else:
        return False


V, E = map(int, sys.stdin.readline().split())

# 입력받은 정보들을 weight 기준으로 정렬
node_list = []
for i in range(E):
    v1, v2, weight = map(int, sys.stdin.readline().split())
    node = (v1, v2, weight)
    node_list.append(node)

node_list = sorted(node_list, key=lambda x: x[2])

# 각 노드들의 parent 정보
parent = [x for x in range(V + 1)]

# weight가 작은 순으로 노드를 cycle이 생기지 않는선에서 연결
# score 값 누적
# cycle 이 생기면 건너뛰고 모든 노드를 연결하면 종료
score = 0
for i in range(E):
    v1 = node_list[i][0]
    v2 = node_list[i][1]
    w = node_list[i][2]

    if not is_same_parent(v1, v2):
        score += w
        union(v1, v2)

print(score)
