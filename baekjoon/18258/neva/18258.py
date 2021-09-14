from sys import stdin

class Queue:

  def __init__(self):
    self.queue = list()
    self.qbp = 0

  def push(self, x):
    self.queue.append(x)
  
  def pop(self):
    if self.empty():
      return -1
    else:
      self.qbp += 1
      return self.queue[self.qbp - 1]

  def size(self):
    return len(self.queue) - self.qbp

  def empty(self):
    if self.size() == 0:
      return 1
    else:
      return 0

  def front(self):
    if self.empty():
      return -1
    else:
      return self.queue[self.qbp]

  def back(self):
    if self.empty():
      return -1
    else:
      return self.queue[-1]

queue = Queue()
for _ in range(int(stdin.readline())):
  cmd_args = stdin.readline().split()

  if cmd_args[0] == "push":
    getattr(queue, cmd_args[0])(cmd_args[1])
  else:
    print(getattr(queue, cmd_args[0])())
