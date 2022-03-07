def solution(genres, plays):
    answer = []
    stream = sorted(list(zip(genres, plays, list(range(len(genres))))), key = lambda x : (x[0], -x[1], x[2]))
    res = []
    temp = [0]
    for i in range(len(stream)):
        temp[0] += stream[i][1]
        temp.append(stream[i][2])
        if i == len(stream) - 1 or stream[i][0] != stream[i+1][0]:
            res.append(temp)
            temp = [0]
    res = sorted(res, key = lambda x : -x[0])
    print(res)
    for j in res:
        for k in j[1:3]:
            answer.append(k)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))