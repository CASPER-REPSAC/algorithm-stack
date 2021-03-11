num = int(input())

result = []
for i in range(num):
    data = []
    check = True

    input_data = input()

    for d in input_data:
        if d == ")":
            if len(data) == 0 or data[len(data) - 1] != "(":
                check = False
                break
            else:
                data.pop(len(data) - 1)
        else :
            data.append(d)
    
    if check == False or len(data) != 0:
        result.append("NO")
    else:
        result.append("YES")


print("\n".join(result))