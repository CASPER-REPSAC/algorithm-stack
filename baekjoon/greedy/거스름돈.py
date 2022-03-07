import sys
input = sys.stdin.readline

def solution(n):
    answer = 0
    if n < 5:
        if n % 2 != 0:
            answer = -1
        else:
            answer = n // 2
    else:
        ct = n // 5
        n = n % 5
        if n == 0:
            answer = ct
        else:
            if n % 2 == 0:
                ct += n // 2
                answer = ct
            else:
                ct += (n + 5) // 2 - 1
                answer = ct
    print(answer)

n = 13
# n = int(input())
solution(n)