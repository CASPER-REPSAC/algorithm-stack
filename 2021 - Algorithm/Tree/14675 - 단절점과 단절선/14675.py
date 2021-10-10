import sys
input = sys.stdin.readline

# 단절점 : 리프노드를 제외한 나머지 노드 즉 연결된 선이 1개 초과면 단절점
# 단절선 : 모든 간선이 단절선

n = int(input())

tree = [0]*n

for _ in range(n-1):
    point1,point2 = map(int,input().split())
    tree[point1-1]+=1
    tree[point2-1]+=1

n2 = int(input())

for _ in range(n2):
    question, value = map(int,input().split())
    if question == 1:
        if tree[value-1]>1:
            print("yes")
        else:
            print("no")
    else:
        print("yes")



    