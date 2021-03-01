import sys

num = int(sys.stdin.readline().strip())

size = 0
stack = []

for i in range(num):
    value = sys.stdin.readline().strip().split(" ")

    if value[0] == "push":
        stack.append(value[1])
        size += 1
    elif value[0] == "pop":
        if size == 0: print("-1")
        else:
            print(stack.pop(size-1))
            size -= 1
    elif value[0] == "size": print(size)
    elif value[0] == "empty":
        if size == 0: print("1")
        else: print("0")
    elif value[0] == "top":
        if size == 0: print("-1")
        else: print(stack[size-1])