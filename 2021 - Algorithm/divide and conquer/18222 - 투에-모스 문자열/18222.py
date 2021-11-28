from sys import stdin
input = stdin.readline

k = int(input())

def find(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n%2==0:
        return 1-find(n//2)
    else:
        return find(n//2)

print(find(k-1))