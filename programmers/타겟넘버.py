from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = deque([[numbers[0],0],[-numbers[0],0]])
    while queue:
        v, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([v + numbers[idx], idx])
            queue.append([v -numbers[idx], idx])
        else:
            if v == target:
                answer += 1
    return answer

numbers = [[4,1,2,1],[1,1,1,1,1],[1,1,1]]
target = [4, 3, 3]
for n, t in zip(numbers, target):
    solution(n, t)