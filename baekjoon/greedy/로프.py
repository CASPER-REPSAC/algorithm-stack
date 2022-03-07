import sys
input = sys.stdin.readline

def solution(n, k):
    k.sort(reverse=True)
    for i in range(len(k)):
        k[i] = k[i] * (i + 1)
    answer = max(k)
    
    return answer

k = []
n = int(input())
for _ in range(n):
    k.append(int(input()))

print(solution(n, k))