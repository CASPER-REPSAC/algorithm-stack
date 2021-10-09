import sys
n = int(sys.stdin.readline())
lst = list() #path

non_scost = list()

p = list(range(n+1))

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1

for i in range(n):
    non_scost.append(int(sys.stdin.readline()))
    lst.append([i+1,0,non_scost[i]])

non_cost = list()
for i in range(n):
    non_cost.append(list(map(int,sys.stdin.readline().split(' '))))
    for j in range(i+1,n):
        lst.append([i+1,j+1,non_cost[i][j]])
lst.sort(key=lambda x:x[2])

tree_edges = 0
mst_cost = 0 

while True:
    if tree_edges == n:
        break
    u, v, wt = lst.pop(0)
    if find(u) != find(v):
        union(u, v)
        mst_cost += wt
        tree_edges += 1

print(mst_cost)