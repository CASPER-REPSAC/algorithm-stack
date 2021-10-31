from sys import stdin

N, K = map(int, stdin.readline().strip().split(' '))
arr = [_ for _ in range(1, N+1)]

remove_i = 0
josephus = []
for size in range(N, 0, -1):
  remove_i = (remove_i + (K - 1)) % size
  josephus.append(arr.pop(remove_i))

print("<%s>" % ", ".join(map(str, josephus)))
