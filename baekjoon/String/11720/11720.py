# import sys
# sys.stdin = open("input.txt","rt")
# 개수 입력
s = int(input())
# 문자열 입력
string = input()
# 결과 변수 선언
res = 0
# 각 자리 int변환 후 합연산
for i in string:
	res += int(i)
print(res)
