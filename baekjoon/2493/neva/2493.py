from sys import stdin

N = int(stdin.readline())
tops = [*map(int, stdin.readline().split(' '))]
receivers = [0] * N
unreached_tops = []

for i in range(N-1, -1, -1):
  while unreached_tops and tops[i] > tops[unreached_tops[-1]]:
    receivers[unreached_tops.pop()] = i + 1
  unreached_tops.append(i)

print(*receivers)
