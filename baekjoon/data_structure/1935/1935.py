import sys

sys.stdin = open("baekjoon\data_structure\\1935\input.txt")
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
lst = dict()
stack = []

for i in range(n):
    lst[chr(65+i)] = int(input())

for i in s:
    if i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b + a)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b * a)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    else:
        stack.append(lst[i])

res = '{0:0.2f}'.format(stack[0])
print(res)