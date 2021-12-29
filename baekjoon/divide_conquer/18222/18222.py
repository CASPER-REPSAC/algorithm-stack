import sys
sys.stdin = open("baekjoon\divide_conquer\\18222\input.txt")
input = sys.stdin.readline

k = int(input())

def sol(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    elif (k % 2):
        return 1 - sol(k // 2)
    else:
        return sol(k // 2)

print(sol(k-1))