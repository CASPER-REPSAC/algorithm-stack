def dfs(graph, v, visited):
    visited[v] = True
    for id, value in enumerate(graph[v]):
        if value == 1 and not visited[id]:
            dfs(graph, id, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for id, v in enumerate(visited):
        if not v :
            dfs(computers, id, visited)
            answer += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))