import sys

S = int(sys.stdin.readline())

i = 0
while True:
    S -= i

    if S <= i:
        S += i
        break

    i += 1

print(i)
