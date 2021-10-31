from sys import stdin

N = int(stdin.readline())

square = 2
if N <= 2:
  print(N)
else :
  while True:
    square *= 2
    if N <= square:
      print((N - (square // 2)) * 2)
      break
