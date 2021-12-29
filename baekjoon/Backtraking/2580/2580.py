import sys

sys.stdin = open("algorithm-stack\\baekjoon\Backtraking\\2580\input.txt","rt")
# 스도쿠 입력
M = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
# 0 좌표 모음
zeros = [(i,j) for i in range(9) for j in range(9) if M[i][j] == 0]

def solve(i, j):
    nums = [1,2,3,4,5,6,7,8,9]

    # 가로 세로 체크
    for k in range(9):
        if M[i][k] in nums:
            nums.remove(M[i][k])
        if M[k][j] in nums:
            nums.remove(M[k][j])

    # 3x3 행렬 체크
    i = i // 3
    j = j // 3
    for y in range(i*3, (i+1)*3):
        for x in range(j*3, (j+1)*3):
            if M[y][x] in nums:
                nums.remove(M[y][x])
    
    return nums

# 답이 출력 여부
flag = False
def dfs(x):
    global flag
    
    # 출력되었다면
    if flag:
        return
    
    # 모든 0을 다 처리했을 때
    if x == len(zeros):
        for row in M:
            # 답 출력
            print(*row)
        flag = True
        return
    
    else:
        (i, j) = zeros[x] # 0의 좌표
        nums = solve(i, j) # 가능성 있는 숫자들 계산

        # 가능성 있는 숫자들을
        for num in nums:
            M[i][j] = num # 가능성 있는 숫자를 넣음
            dfs(x + 1) # 다음 0으로 들어감
            M[i][j] = 0 # 아니라면 다시 0으로

dfs(0)