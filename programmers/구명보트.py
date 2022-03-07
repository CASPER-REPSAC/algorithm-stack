"""def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    while people:
        tmp = people.pop(0)
        for i in range(len(people)):
            if people[i] + tmp <= limit:
                people.pop(i)
                break
        answer += 1
    return answer"""

"""def solution(people, limit):
    people.sort()
    answer = 0
    while people:
        tmp = people.pop()
        if people and tmp + people[0] <= limit:
            people.pop(0)
        answer += 1
    return answer"""

def solution(people, limit):
    people.sort()
    answer = 0
    start = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer

people = [70, 80, 50]
limit = 100
print(solution(people, limit))