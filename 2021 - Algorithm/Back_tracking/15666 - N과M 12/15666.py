from sys import stdin
input = stdin.readline

n, m = map(int,input().split())
numbers = list(set(map(int,input().split())))
numbers.sort()
arr = []

def make(count):
    if count == m:
        print(" ".join(map(str,arr)))
    
    for i in 

make(0)