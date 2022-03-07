def solution(n):
    answer = n
    count = bin(n).count('1')
    while True:
        answer += 1
        if bin(answer).count('1') == count:
            break
    return answer

print(solution(78))