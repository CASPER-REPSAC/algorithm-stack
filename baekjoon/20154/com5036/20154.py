"""
1. 문자열이 주어짐(대문자)
2. 문자의 획수로 문자를 변환
3. 앞에서부터 두 개씩 더해감 짝이 지어지지 않으면 그대로 다음 단계
4. 앞의 과정 반복
5. 10이 넘으면 10으로 나눈 나머지
6. 마지막 수가 짝수면 패배 홀수면 승리
"""

CLASSES = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 3, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3,
           'N': 3, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 2, 'X': 2, 'Y': 2, 'Z': 1}


# 2. 획수로 변환
def string_to_num(st):
    num = []
    for ch in st:
        num.append(CLASSES[ch])
    return num


# 3. 앞에서부터 두 개씩 더해감
def add(num):
    if len(num) % 2 == 1:
        num.append(0)

    result = []
    for i in range(0, len(num), 2):
        result.append((num[i] + num[i + 1]) % 10)

    return result


def is_victory(num):
    if num[0] % 2 == 1:
        print("I'm a winner!")
    else:
        print("You're the winner?")


if __name__ == "__main__":
    string = input()

    num = string_to_num(string)

    while len(num) > 1:
        num = add(num)

    is_victory(num)
