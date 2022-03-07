import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(19)]

flag = False

def check_dir(c, x, y):
    dir = []
    dx = [0, 1, 1, 1]
    dy = [1, 1, 0, -1]
    for i in range(4):
        if board[x + dx[i]][y + dy[i]] == c:
            dir.append([dx[i], dy[i]])
    return dir

def recursion(c, x, y, dir, cnt):
    global flag
    dx, dy = dir
    cnt += 1
    if cnt == 5:
        if not board[x + dx][y + dy] == c:
            flag = True
            print(c)
            print(x - (dx * 3), y - (dy * 3))
            return
    elif board[x + dx][y + dy] == c:
        recursion(c, x+dx, y+dy, dir, cnt)
    return


def solution(board):
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                dir = check_dir(1, i, j)
                for d in dir:
                    recursion(1, i, j, d, 0)
            elif board[i][j] == 2:
                dir = check_dir(2, i, j)
                for d in dir:
                    recursion(2, i, j, d, 0)
    if not flag:
        print(ans)

solution(board)