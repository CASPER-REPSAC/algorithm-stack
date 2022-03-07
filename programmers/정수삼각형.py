def solution(triangle):
    for i in range(len(triangle) - 1, -1, -1):
        for j, l, r in zip(range(len(triangle[i-1])), triangle[i], triangle[i][1:]):
            triangle[i-1][j] = max(triangle[i-1][j] + l, triangle[i-1][j] + r)
    answer = triangle[0][0]
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))