import sys
from collections import deque

sys.stdin = open("baekjoon\data_structure\\10866\input.txt")

d = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = list(sys.stdin.readline().strip().split(" "))
    
    if cmd[0] == 'push_front':
        d.appendleft(cmd[1])
        
    elif cmd[0] == 'push_back':
        d.append(cmd[1])
        
    elif cmd[0] == 'pop_front':
        if d:
            tmp = d.popleft()
            print(tmp)
        else:
            print("-1")
            
    elif cmd[0] == 'pop_back':
        if d:
            tmp = d.pop()
            print(tmp)
        else:
            print("-1")
            
    elif cmd[0] == 'size':
        print(len(d))
        
    elif cmd[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
            
    elif cmd[0] == 'front':
        if d:
            print(d[0])
        else:
            print("-1")
        
    elif cmd[0] == 'back':
        if d:
            print(d[len(d)-1])
        else:
            print("-1")
    