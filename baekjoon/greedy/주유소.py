import sys
input = sys.stdin.readline

def solution(price, graph):
    answer = 0
    for i in range(len(graph)):
        distance = 0
        for j in range(i, len(graph)):
            if price[i] < price[i + 1]:
                answer += distance * price[i]
        print()
    return answer

n = 4
graph = [2, 3, 1]
price = [5,2,4,1]
"""n = int(input())
graph = list(map(int, input().split()))
price = list(map(int, input().split()))"""
print(solution(price, graph))