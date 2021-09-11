# import sys
# sys.stdin = open("input.txt", "rt")

# 그룹체크 판단
def groupCheck(str):
	first = ""
	w = dict()
	for j in str:
		if j is not first:
			if j in w:
				return 0
			else:
				w[j] = 1
				first = j
	else:
		return 1
# 결과
res = 0
# 단어장 리스트
words = []
# 단어 개수 입력
n = int(input())
# 단어 입력받기
for _ in range(n):
	words.append(input())
# 그룹 판단
for i in words:
	res += groupCheck(i)
# 결과 출력
print(res)
