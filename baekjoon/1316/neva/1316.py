from sys import stdin

words_num = int(stdin.readline())

def is_group_word(word):
  pre = ''
  pre_chars = []
  for char in word:
    if pre != char:
      if char not in pre_chars:
        pre_chars.append(char)
      else:
        return False
      pre = char
  return True

cnt_group_word = 0
for _ in range(words_num):
  if is_group_word(stdin.readline().strip()):
    cnt_group_word += 1

print(cnt_group_word)
