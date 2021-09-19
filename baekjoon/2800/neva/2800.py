import itertools
from sys import stdin
from itertools import combinations

exp = [* stdin.readline().strip()]
open_parenthesis_idx_stack, parentheses_idx, expressions = [], [], set()

for i, char in enumerate(exp):
  if char == '(':
    open_parenthesis_idx_stack.append(i)
  elif char == ')':
    parentheses_idx.append((open_parenthesis_idx_stack.pop(), i))

for i in range(1, len(parentheses_idx) + 1):
  parentheses_combinations = itertools.combinations(parentheses_idx, i)
  for parentheses_combination in parentheses_combinations:
    exp_tmp = exp[:]
    for open_p_idx, close_p_idx in parentheses_combination:
      exp_tmp[open_p_idx] = ''
      exp_tmp[close_p_idx] = ''
    expressions.add(''.join(exp_tmp))

for exp in sorted(list(expressions)):
  print(exp)
