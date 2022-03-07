prices = [1, 2, 3, 2, 3]
answer = [0 for _ in range(len(prices))]
stack = []

for i in range(len(prices)):
    while stack and prices[stack[-1]] > prices[i]:
        tmp = stack.pop()
        answer[tmp] = i - tmp
    stack.append(i)

while stack:
    tmp = stack.pop()
    answer[tmp] = len(prices) - 1 - tmp