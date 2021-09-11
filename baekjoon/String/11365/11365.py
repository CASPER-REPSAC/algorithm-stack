# import sys
# sys.stdin = open("input.txt", "rt")
# 입력 리스트
note = []
# 입력
while True:
	str = input()
	if(str == "END"):
		break
	note.append(str)
# 반대로 출력
for i in note:
	i = i[::-1]
	print(i)
