from sys import stdin


class Stack:
    def __init__(self):
        self.stack = list()
        self.stack_size = 0

    def push(self, x):
        self.stack.append(x)
        self.stack_size += 1

    def pop(self):
        if self.empty():
            return -1
        else:
            self.stack_size -= 1
            return self.stack.pop()

    def size(self):
        return self.stack_size

    def empty(self):
        if self.stack_size == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]


stack = Stack()

N = int(stdin.readline())
for _ in range(N):
    cmd_args = stdin.readline().split()

    if cmd_args[0] == "push":
        getattr(stack, cmd_args[0])(cmd_args[1])
    else:
        print(getattr(stack, cmd_args[0])())
