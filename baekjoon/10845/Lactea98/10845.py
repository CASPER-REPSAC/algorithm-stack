import sys

queue = []
num = int(sys.stdin.readline().strip())

for _ in range(num):
    command = sys.stdin.readline().strip().split(" ")

    if command[0] == "push": queue.append(command[1])
    elif command[0] == "pop": print("-1" if len(queue) == 0 else queue.pop(0))
    elif command[0] == "size": print(len(queue))
    elif command[0] == "empty": print("1" if len(queue) == 0 else "0")
    elif command[0] == "front": print("-1" if len(queue) == 0 else queue[0])
    elif command[0] == "back": print("-1" if len(queue) == 0 else queue[len(queue)-1])