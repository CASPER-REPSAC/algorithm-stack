from sys import stdin

num = int(stdin.readline().strip())
input_val = []
for _ in range(num):
    input_val.append(int(stdin.readline().strip()))

compare = []
result = []
for i in range(num):
    compare.append(i+1)
    result.append("+")
    
    for j in range(len(compare)):
        if compare[len(compare) - 1] == input_val[0]:
            compare.pop(len(compare) - 1)
            input_val.pop(0)
            result.append("-")
        elif compare[len(compare) - 1] > input_val[0]:
            break
        else:
            break

if len(input_val) != 0: print("NO")
else: print("\n".join(result))