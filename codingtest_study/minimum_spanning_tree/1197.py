import sys
n, ed = map(int,sys.stdin.readline().split(' '))
lst = list() #path
p = list(range(n+1))

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1

for i in range(ed):
    lst.append(list(map(int,sys.stdin.readline().split(' '))))
lst.sort(key=lambda x:x[2])

tree_edges = 0
mst_cost = 0 

while True:
    if tree_edges == n-1:
        break
    u, v, wt = lst.pop(0)
    if find(u) != find(v):
        union(u, v)
        mst_cost += wt
        tree_edges += 1

print(mst_cost)