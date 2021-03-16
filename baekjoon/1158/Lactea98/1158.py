from sys import stdin

num = list(map(int, stdin.readline().strip().split(" ")))
arr = list(map(int, range(1, num[0]+1)))
result = []

index = 0
while True:
    for _ in range(num[1] - 1):
        arr.append(arr.pop(0))
    result.append(str(arr.pop(0)))

    if len(arr) == 1:
        result.append(str(arr.pop(0)))
        break

print("<" + ", ".join(result) + ">")