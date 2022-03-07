def solution(name):
    names = [ord(i) - ord('A') if ord(i) < 78 else ord('Z') - ord(i) + 1 for i in name]
    lrmin = len(name) - 1
    answer = sum(names)

    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        lrmin = min(lrmin, (i * 2) + len(name) - next)

    for i in range(len(name) - 1, 0 , -1):
        next = i - 1
        while next >= 0 and name[next] == 'A':
            next -= 1
        lrmin = min(lrmin, (len(name) - i) * 2 + next)

    answer += lrmin
    return answer

name = "BBBBAAAAAB"
print(solution(name))