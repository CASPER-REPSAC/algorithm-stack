length = int(input())

for i in range(length):
    value = input().split(" ")
    print(" ".join(word[::-1] for word in value))