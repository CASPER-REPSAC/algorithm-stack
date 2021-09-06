from sys import stdin


class Editor:
    def __init__(self, data):
        self.left_stack = list(data)
        self.right_stack = list()

    def print(self):
        print(''.join(self.left_stack + self.right_stack[::-1]))

    def left_cursor(self):
        if self.left_stack:
            self.right_stack.append(self.left_stack.pop())

    def right_cursor(self):
        if self.right_stack:
            self.left_stack.append(self.right_stack.pop())

    def press(self, data):
        self.left_stack.append(data)

    def backspace(self):
        if self.left_stack:
            self.left_stack.pop()


editor = Editor(stdin.readline().strip())
for _ in range(int(stdin.readline())):
    cmd_args = stdin.readline().split()

    if cmd_args[0] == "L":
        editor.left_cursor()
    elif cmd_args[0] == "D":
        editor.right_cursor()
    elif cmd_args[0] == "B":
        editor.backspace()
    elif cmd_args[0] == "P":
        editor.press(cmd_args[1])

editor.print()
