import sys
input = sys.stdin.readline

def solution(str):
    str = str.replace("XXXX", "AAAA")
    str = str.replace("XX", "BB")
    if "X" in str:
        print(-1)
    else:
        print(str)

str = "XX.XXXXXXXXXX..XXXXXXXX...XXXXXX"
# str = input()
solution(str)