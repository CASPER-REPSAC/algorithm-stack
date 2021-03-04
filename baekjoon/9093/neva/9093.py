from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    words = stdin.readline().split()

    for word in words:
        print(word[::-1], end=' ')
    print('')
