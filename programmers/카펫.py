brown = 8
yellow = 1

wh = (brown // 2)  + 2
answer = []

answer = [[i, j] for i, j in zip(range(0, wh), range(wh, 0, -1)) if i >= j and (i * j) == (brown + yellow)]
print(answer)