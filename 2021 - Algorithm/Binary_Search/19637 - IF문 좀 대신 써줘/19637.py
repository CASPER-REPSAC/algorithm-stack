import sys
input = sys.stdin.readline


def checkname(name,data):
    result = 0
    start,end = 0, len(name)-1

    while start<=end:
        mid = (start+end)//2
        if int(name[mid][1]) >= data :
            end = mid-1
            result = mid
        else:
            start = mid+1
    return name[result][0]

n,m = map(int,input().split())
name = [input().split() for _ in range(n)]
for _ in range(m):
    data = int(input())
    print(checkname(name,data))