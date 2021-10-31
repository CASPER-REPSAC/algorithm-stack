from sys import stdin

string_num = int(stdin.readline())

for _ in range(string_num):
  chars = {}
  string = list(stdin.readline().strip())

  for char in string:
    if char in chars:
      chars[char] += 1
    elif ' ' != char:
      chars[char] = 1

  max_values = [k for k, v in chars.items() if max(chars.values()) == v]
  
  if 1 < len(max_values):
    print("?")
  else:
    print(max_values[0])
