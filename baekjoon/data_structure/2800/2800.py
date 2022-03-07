import sys
from itertools import combinations

sys.stdin = open("baekjoon\data_structure\\2800\input.txt")
input = sys.stdin.readline

s = input().strip()

stack = []
pair = []
answer = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        tmp = stack.pop()
        pair.append([tmp, i])

for i in range(1, len(pair) + 1):
    for j in list(combinations(pair, i)):
        expt = []
        result = []
        for c in j:
            l, r = c
            expt.append(l)
            expt.append(r)
        for k in range(len(s)):
            if k in expt:
                continue
            else:
                result.append(s[k])
        answer.append(''.join(result))

answer = set(answer)
answer = list(answer)
for a in sorted(answer):
    print(a)