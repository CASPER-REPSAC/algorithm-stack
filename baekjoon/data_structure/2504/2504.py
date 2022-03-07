import sys
sys.stdin = open("baekjoon\data_structure\\2504\input.txt")
input = sys.stdin.readline

s = input().strip()
res = 0

def check(ss):
    stack = []
    for s in ss:
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif s == ']' and stack:
            if stack[-1] == '[':
                stack.pop()
            else:
                return False
        else:
            return False

    if stack:
        return False
    else:
        return True

def sol(ss):
    stack = []
    for s in ss:
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0
                while stack[-1] != '(':
                    tmp += stack.pop()
                stack[-1] = tmp * 2

        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0
                while stack[-1] != '[':
                    tmp += stack.pop()
                stack[-1] = tmp * 3

    return stack

if check(s):
    stack = sol(s)
    for i in stack:
        res += i
    print(res)
else:
    print(0)