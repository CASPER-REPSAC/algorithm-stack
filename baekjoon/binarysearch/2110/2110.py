import sys

sys.stdin = open("algorithm-stack\\baekjoon\\binarysearch\\2110\input.txt")

# 입력
n, c = map(int, sys.stdin.readline().split())
x = []
for _ in range(n):
    x.append(int(sys.stdin.readline()))

# 이분탐색을 위한 정렬
x.sort()
# 이분탐색 시작지점, 끝지점
s, e = 1, x[-1] - x[0]

# 해당 거리 이상유지하며 공유기 설치 확인
def binary_search(distance):
    count = 1
    sx = x[0]
    # 모든 집 확인
    for i in range(1, n):
        # 이전 집에서의 거리보다 멀리 떨어져 있다면 설치
        if sx + distance <= x[i]:
            count += 1
            sx = x[i]
    return count

# 이분 탐색
while s <= e:
    m = (s + e) // 2

    if binary_search(m) >= c:
        res = m
        s = m + 1
    else:
        e = m - 1

print(res)

