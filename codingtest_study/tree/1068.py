import sys
    
n = int(sys.stdin.readline())

tree = list(map(int,sys.stdin.readline().split(' ')))

delnode = int(sys.stdin.readline())

stack = []
stack.append(delnode)
tree[delnode] = 99

while stack != []:
    t = stack.pop()
    for i in range(n):
        if tree[i] == t:
            tree[i] = 99
            stack.append(i)
    

cnt = 0
for i in range(n):
    if i not in tree and tree[i] != 99:
        cnt+=1

print(cnt)
