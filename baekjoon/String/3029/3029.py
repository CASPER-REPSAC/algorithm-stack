import sys
sys.stdin = open("algorithm-stack\\baekjoon\String\\3029\input.txt","rt")

s = list(map(int, input().split(":")))
e = list(map(int, input().split(":")))

st = s[0]*60*60 + s[1]*60 + s[2]
et = e[0]*60*60 + e[1]*60 + e[2]

if et > st:
    t = et - st
else:
    t = et - st + (24*60*60)

h = t // 60 // 60
m = t // 60 % 60
s = t % 60
print("%02d:%02d:%02d" % (h,m,s))