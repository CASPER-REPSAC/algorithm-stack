import sys
sys.stdin = open("algorithm-stack\\baekjoon\\binarysearch\\2417\input.txt")

n = int(sys.stdin.readline())
s, e = 0, n

while s <= e:
    m = (s + e) // 2
    if m * m < n:
        s = m + 1
    else:
        e = m - 1

print(s)