import sys
from collections import deque

sys.stdin = open("baekjoon\data_structure\\1874\input.txt")
input = sys.stdin.readline

n = int(input())
stack = deque()
result = deque()
top = 1

for i in range(n):
    num = int(input())
    while top <= num:
        stack.append(top)
        result.append('+')
        top += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
        
    else:
        print("NO")
        break

else:
    for i in result:
        print(i)