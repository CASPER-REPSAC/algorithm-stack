import sys
from collections import deque
sys.stdin = open("baekjoon\data_structure\\2493\input.txt")
input = sys.stdin.readline

n = int(input())
top = deque(map(int, input().split()))
stack = []
answer = [0 for _ in range(len(top))]

for i in range(n):
    print(stack)
    while stack and top[stack[-1]] < top[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)

for i in answer:
    print(i, end=' ')