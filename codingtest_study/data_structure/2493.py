import sys

lst = []
stack = []
result = ""

n = int(sys.stdin.readline())

lst = sys.stdin.readline().split(" ")

stack.append([int(lst[0]), 0])
result += "0 "
for i in range(1, n):
    while stack[-1][0] < int(lst[i]) :
        stack.pop()
        if stack == [] :
            break
    if stack == [] :
        result += "0 "
    else :
        result += str(stack[-1][1] + 1) + " "
    stack.append([int(lst[i]),i])

print(result)