import sys

n, m = map(int, sys.stdin.readline().split())

"""
# 시간 3820 ms
string_set = [sys.stdin.readline().strip() for i in range(n)]
check_set = [sys.stdin.readline().strip() for j in range(m)]

count = 0
for string in check_set:
    if string in string_set:
        count += 1

print(count)
"""

# 시간 152 ms
string_set = {}
for i in range(n):
    string_set[sys.stdin.readline().strip()] = 1

count = 0
for j in range(m):
    if string_set.get(sys.stdin.readline().strip(), 0):
        count+=1
print(count)

