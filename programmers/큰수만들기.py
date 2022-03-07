"""from itertools import combinations

def solution(number, k):
    answer = 0
    lst = list(combinations([i for i in range(len(number))], len(number) - k))
    for i in lst:
        comb = ''
        for j in range(len(number) - k):
            comb += number[i[j]]
        if int(answer) < int(comb):
            answer = comb
    return str(answer)"""

"""def solution(number, k):
    answer = []
    excpt = []
    m = max(number[:k])
    id = number.index(m)
    k -= id

    for i in range(id):
        excpt.append(i)
    
    for i in range(len(number[id:]) - 1):
        if k == 0:
            break
        if int(number[id + i]) < int(number[id + i + 1]):
            excpt.append(id + i)
            k -= 1
    else:
        while k > 0:
            excpt.append(number.index(min(number[id:])))
            k -= 1
        
    for i in range(len(number)):
        if i not in excpt:
            answer.append(number[i])
    answer = ''.join(answer)
    return answer"""

def solution(number, k):
    answer = []
    for num in number:
        print(answer)
        while k > 0 and answer and num > answer[-1]:
            answer.pop()
            k -= 1
        answer.append(num)
    answer = ''.join(answer)
    return answer[:len(number) - k]

number = "654321"
k = 5
print(solution(number, k))