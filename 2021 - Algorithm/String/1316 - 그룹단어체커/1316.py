count = int(input())
cnt = 0
for i in range(count):
    charlist = []
    string = input()
    for i in range(len(string)):
        if string[i] in charlist:
            if string[i-1] == string[i]:
                continue
            else:
                cnt-=1
                break
        else:
            charlist.append(string[i])
    cnt+=1

print(cnt)
