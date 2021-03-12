from sys import stdin

stack1 = list(stdin.readline().strip())
stack2 = []
for _ in range(int(stdin.readline().strip())):
    command = stdin.readline().strip().split(" ")
    if command[0] == "P": stack1.append(command[1])
    elif command[0] == "L" and len(stack1) != 0: stack2.append(stack1.pop())
    elif command[0] == "D" and len(stack2) != 0: stack1.append(stack2.pop())
    elif command[0] == "B" and len(stack1) != 0: stack1.pop()
print("".join(stack1) + "".join(stack2[::-1]))