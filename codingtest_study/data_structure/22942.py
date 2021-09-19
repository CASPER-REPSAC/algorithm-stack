import sys 

n = int(sys.stdin.readline())

lst = dict()
result = "YES"

for i in range(n):
    c = sys.stdin.readline().split()
    x = int(c[0]) - int(c[1])
    y = int(c[0]) + int(c[1])
    if (x in lst and y not in lst) or (x not in lst and y in lst):
        result = "NO"
        break
    elif x in lst and y in lst:
        if lst[x] != lst[y]:
            result = "NO"
            break
        elif x-1 not in lst or y+1 not in lst:
            result = "NO"
            break
    else :
        for j in range(x,y+1):
            lst[j] = i

print(result)