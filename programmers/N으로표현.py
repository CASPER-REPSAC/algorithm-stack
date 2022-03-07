def solution(N, number):
    if N == number:
        return 1
    dp = [0, {N}]
    for i in range(2, 9):
        tmp = set()
        tmp.add(int(str(N) * i))
        for j, k in zip(range(1, i), range(i - 1, 0, -1)):
            for l in dp[j]:
                for m in dp[k]:
#                    if i == 5 and k == 1:
#                        print(i,j,k, l, m)
                    tmp.add(l+m)
                    tmp.add(l-m)
                    tmp.add(m-l)
                    tmp.add(l*m)
                    if l != 0 and m != 0:
                        tmp.add(l//m)
                        tmp.add(m//l)
        if number in tmp:
            return i
        dp.append(tmp)
    return -1

N = 4
number = 9
#print(solution(N, number))
#print(solution(1,1121),7)
#print(solution(5,1010),7)
#print(solution(7,7784),5)
#print(solution(2,22223),7)
#print(solution(2,22224),6)
#print(solution(2,11111),6)