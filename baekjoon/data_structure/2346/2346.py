import sys
from collections import deque
sys.stdin = open("baekjoon\data_structure\\2346\input.txt")
input = sys.stdin.readline

n = int(input())
balloon = deque(enumerate(map(int, input().split())))

while balloon:
    num, rt = balloon.popleft()
    print(num + 1, end=' ')
    if rt > 0:
        balloon.rotate(-(rt-1))
    else:
        balloon.rotate(-rt)