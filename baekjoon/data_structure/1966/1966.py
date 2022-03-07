import sys
from collections import deque
sys.stdin = open("baekjoon\data_structure\\1966\input.txt")
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    order = 0
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    p = deque(0 for _ in range(n))
    p[m] = 1
    
    while True:
        if q[0] == max(q):
            order += 1

            if p[0] != 1:
                q.popleft()
                p.popleft()
            else:
                print(order)
                break
        else:
            tmp = q.popleft()
            q.append(tmp)
            tmp = p.popleft()
            p.append(tmp)