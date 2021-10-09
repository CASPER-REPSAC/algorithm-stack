import sys


# 노드의 부모를 반환
def get_parent(x):
    if x == parent[x]:
        return parent[x]
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]


# 두 노드를 연결
def union(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 같은 그래프에 있는지
def is_same_network(a, b):
    if get_parent(a) == get_parent(b):
        return True
    return False


N = int(sys.stdin.readline())  # 컴퓨터의 수
M = int(sys.stdin.readline())  # 연결할 수 있는 선의 수
parent = [i for i in range(N + 1)]  # 각 노드의 부모

# 연결할 정보들을 입력 받음
network = []
for _ in range(M):
    com1, com2, cost = map(int, sys.stdin.readline().split())
    network.append((com1, com2, cost))

# 비용이 낮은 순으로 정렬
network = sorted(network, key=lambda x: x[2])

# 낮은 비용부터 연결 하면서 비용을 누적
min_cost = 0
for i in range(M):
    com1 = network[i][0]
    com2 = network[i][1]
    cost = network[i][2]

    # cycle 이 생기면 건너뜀
    if is_same_network(com1, com2):
        continue

    union(com1, com2)
    min_cost += cost

print(min_cost)
