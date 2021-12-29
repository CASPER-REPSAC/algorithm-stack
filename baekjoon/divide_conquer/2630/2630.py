import sys
sys.stdin = open("baekjoon\divide_conquer\\2630\input.txt")
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def sol(x, y, n):
    global white, blue
    color = a[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != a[i][j]:
                sol(x, y, n // 2) # 1사분면
                sol(x, y + (n // 2), n // 2) # 2사분면
                sol(x + (n // 2), y, n // 2) # 3사분면
                sol(x + (n // 2), y + (n // 2), n // 2) # 4사분면
                return

    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return

sol(0, 0, n)
print(white)
print(blue)