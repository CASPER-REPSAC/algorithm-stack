import sys

sys.stdin = open("algorithm-stack\\baekjoon\Backtraking\\15649\input.txt","rt")
n, m = map(int, input().split())
# 조합 리스트
choose = [ 0 for _ in range(9)]
# 사용된 숫자 체크
used = [ 0 for _ in range(9)]

def solve(cnt):
    global n, m
    # choose에 m개를 담았다면
    if cnt == m:
        # 출력
        for i in range(cnt):
            print(choose[i], end=' ')
        print()
        return

    # 1부터 n까지 자연수 중
    for i in range(1, n+1):
        # 중복 없이이므로 사용되었다면 넘김
        if used[i]:
            continue
        # 사용 체크
        used[i] = 1
        # 조합 리스트에 넣기
        choose[cnt] = i
        # 다음 자리에 올 숫자 재귀
        solve(cnt + 1)
        # 나온 후 사용 철회
        used[i] = 0

solve(0)