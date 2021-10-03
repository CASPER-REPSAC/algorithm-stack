import sys

n = int(sys.stdin.readline())
tree = [[0] * 2 for i in range(n + 1)]
level = [[] for i in range(n + 1)]
froot = [0 for i in range(n + 1)]
num = 1

def inorder(node, lv):
    global num
    left = tree[node][0]
    right = tree[node][1]
    if tree[node][0] != -1:
        inorder(left, lv + 1)
    level[lv].append(num)
    num+=1
    if tree[node][1] != -1:
        inorder(right, lv + 1)

for i in range(n):
    node, left, right = map(int,sys.stdin.readline().split(' '))
    tree[node][0] = left
    tree[node][1] = right
    froot[node] +=1
    if left != -1 : froot[left]+=1
    if right != -1 : froot[right]+=1

for i in range(1, n+1):
    if froot[i] == 1 :
        root = i
        
inorder(root, 1)
result = 0
l = 0
for i in range(1,n + 1):
    if level[i]:
        sub = max(level[i]) - min(level[i]) + 1
        if result < sub :
            result = sub
            l = i

print(l, result)
# inorder
# (레벨, 위치좌표)