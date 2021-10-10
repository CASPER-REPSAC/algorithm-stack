from sys import stdin
input = stdin.readline

#크루스칼 알고리즘 사용

def find(p,x):
    if p[x] != x:
        p[x] = find(p,p[x])
    return p[x]

def union(p,x,y):
    x = find(p,x)
    y = find(p,y)

    if x > y:  # 부모가 다르면 부모를 합쳐버림
        p[x] = y
    else:
        p[y] = x

point, line = map(int,input().split())
original = []
p = [0]

for i in range(1,point+1):  # 최소신장트리를 위한 집합 생성
    p.append(i)


for _ in range(line):      
    a,b,weight = map(int,input().split())
    original.append([weight,a,b])  # 가중치를 기준으로 정렬위함

original.sort() 
# 위에서 weight 를 먼저 저장안해도 original.sort(key = lamda x:x[2]) 이렇게 할 수도 있다.

count = 0
weightsum = 0
while original:
    if count == point-1:
        break

    weight,a,b = original.pop(0)
    
    if find(p,a) != find(p,b):
        union(p,a,b)
        count+=1
        weightsum += weight

print(weightsum)
