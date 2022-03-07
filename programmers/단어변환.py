"""from collections import deque

def count_check(graph, begin, words):
    count = []
    for w in range(len(words)):
        tmp = 0
        for i, j in zip(begin, words[w]):
            if i != j:
                tmp += 1
        count.append(tmp)
    count = [id for id, v in enumerate(count) if v == 1]
    graph.append(count)

def bfs(graph, start, visited, words, target):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                print(words[i], cnt)
                if words[i] == target:
                    return cnt
                queue.append(i)
                visited[i] = True
    else:
        return 0

def solution(begin, target, words):
    answer = 0
    words = deque(words)
    words.appendleft(begin)
    graph = []
    for i in words:
        count_check(graph, i, words)
    visited = [False] * len(words)
    answer = bfs(graph, 0, visited, words, target)
    return answer
"""
from collections import deque

def solution(begin, target ,words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visited = [False for i in range(len(words))]

    if target not in words:
        answer = 0
        return answer
    else:
        while q:
            word, cnt = q.popleft()
            if word == target:
                answer = cnt
                break
            for w in range(len(words)):
                tmp = 0
                for i, j in zip(word, words[w]):
                    if i != j:
                        tmp += 1
                if tmp == 1:
                    q.append([words[w], cnt+1])
                    visited[w] == True
        return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))