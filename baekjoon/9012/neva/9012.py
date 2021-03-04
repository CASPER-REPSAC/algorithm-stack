from sys import stdin


def is_vps(parenthesis_string):
    open_cnt = 0
    for parenthesis in parenthesis_string:
        if parenthesis == '(':
            open_cnt += 1
        else:
            if open_cnt == 0:
                return False
            else:
                open_cnt -= 1

    if open_cnt == 0:
        return True
    else:
        return False


T = int(stdin.readline())

for _ in range(T):
    if is_vps(stdin.readline().strip()):
        print("YES")
    else:
        print("NO")
