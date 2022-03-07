n = 5
lost = [1,2,3,5]
reserve = [1,2,3,4]

_lost = list(set(lost) - set(reserve)) # [i for i in lost if i not in reserve]
_reserve = list(set(reserve) - set(lost)) # [i for i in reserve if i not in lost]

print(_lost, _reserve)

for i in _reserve:
    if i - 1 in _lost:
        _lost.remove(i - 1)
    elif i + 1 in _lost:
        _lost.remove(i + 1)

answer = n - len(_lost)
print(answer)