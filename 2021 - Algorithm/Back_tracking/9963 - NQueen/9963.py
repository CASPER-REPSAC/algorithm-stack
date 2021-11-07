from sys import stdin
input = stdin.readline

#시간 초과

count = 0
n = int(input())
def check(index, board):
    global count

    if(index == n):
        count+=1
    else:
        for i in range(n):
            board[index] = i
            if (possible(index,board)):
                check(index+1,board)

def possible(index,board):
    for i in range(index):
        if (board[index] == board[i]) or (index - i == abs(board[index] - board[i])):
            return False
    return True

board = [0] * n
check(0, board)
print(count)

