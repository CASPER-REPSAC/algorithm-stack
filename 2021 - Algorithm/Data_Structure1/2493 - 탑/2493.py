from sys import stdin

n = int(stdin.readline())
top = list(map(int,stdin.readline().split()))#6 9 5 7 4
stack = []
answer = []
for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:  
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  
        answer.append(0)
    stack.append([i, top[i]])

print(" ".join(map(str, answer)))

    
    