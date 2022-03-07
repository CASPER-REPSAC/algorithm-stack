import itertools
import math

numbers = "011"
nums = [i for i in numbers]
answers = []

def is_prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(1, len(nums) + 1):
    p = itertools.permutations(numbers, i)
    for j in p:
        answers.append(''.join(j))

answers = list(set(int(i) for i in answers if is_prime(int(i)) is True))
answer = len(answers)
print(answers, answer)