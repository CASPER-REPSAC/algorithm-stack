import sys

lst = []
result = ""

n = int(sys.stdin.readline())

lst_t = sys.stdin.readline().split(" ")
lst = []
for i in range(n):
    lst.append([int(lst_t[i]), i + 1])

index = 0

while lst != []:
    if index >= n or index < 0:
        index %= n
    
    t = lst[index][0]
    if lst[index][0] > 0:
        t -= 1
    result += str(lst[index][1]) + " "
    del lst[index]
    index += t
    n -= 1

print(result)