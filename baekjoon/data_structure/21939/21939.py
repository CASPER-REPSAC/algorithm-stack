import sys
import heapq
sys.stdin = open("baekjoon\data_structure\\21939\input.txt")
input = sys.stdin.readline

min_heap = []
max_heap = []
n = int(input())
check_list = dict()

for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))
    check_list[p] = True

m = int(input())
command = [input().split() for _ in range(m)]
for com in command:
    if com[0] == 'recommend':
        if com[1] == '1':
            while not check_list[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        elif com[1] == '-1':
            while not check_list[min_heap[0][1]]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])

    elif com[0] == 'add':
        p, l = map(int, com[1:])
        while not check_list[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        while not check_list[min_heap[0][1]]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, (l, p))
        heapq.heappush(max_heap, (-l, -p))
        check_list[p] = True

    elif com[0] == 'solved':
        p = int(com[1])
        check_list[p] = False