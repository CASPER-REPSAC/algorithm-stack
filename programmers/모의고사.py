answers = [1,3,2,4,2]

p = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
s = []
answer = []

for i in range(3):
    tmp = 0
    for j in range(len(answers)):
        if answers[j] == p[i][j % len(p[i])]:
            tmp += 1
    s.append(tmp)

answer = [i for i, value in enumerate(s, start=1) if value == max(s)]
answer.sort()

print(s, answer)