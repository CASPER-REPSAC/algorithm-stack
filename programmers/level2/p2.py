from collections import Counter

def solution(clothes):
    answer = 1
    cloth = Counter([kind for name, kind in clothes])
    for i in cloth.values():
        answer *= i + 1
    return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))