from sys import stdin
from collections import deque

N = int(stdin.readline())
ballon = deque(enumerate(map(int,stdin.readline().split()))) 
# ennumerate : 인덱스와 같이 튜플로 저장
while True:
    index, data = ballon.popleft()
    print(index+1,end=' ')

    if not ballon:
        break

    if data >0: #rotate : 양수는 오른쪽으로 음수는 왼쪽으로 회전
        ballon.rotate(-(data-1))

    elif data<0:
        ballon.rotate(-data)
