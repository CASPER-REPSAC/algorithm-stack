# import sys
# sys.stdin = open("input.txt", "rt")
# 문자열 저장할 리스트
words = []
# 개수 입력
s = int(input())
# 단어 입력
for _ in range(s):
	words.append(input())

# 중복 제거
words = list(set(words))
# 문자길이 우선 정렬
words.sort(key = lambda x: (len(x), x))
#결과 출력
for i in words:
	print(i)
