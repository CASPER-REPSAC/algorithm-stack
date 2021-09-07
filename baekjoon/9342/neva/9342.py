from sys import stdin
import re

infection_regex = re.compile(r'^[A-F]?A+F+C+[A-F]?$')

for _ in range(int(stdin.readline())):
  if infection_regex.match(stdin.readline().strip()):
    print("Infected!")
  else:
    print("Good")
