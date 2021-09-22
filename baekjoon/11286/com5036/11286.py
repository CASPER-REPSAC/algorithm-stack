import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for i in range(n):
    input_num = int(sys.stdin.readline())

    if input_num == 0:
        if not heap:
            print(0)
            continue

        max_num = heapq.heappop(heap)[1]
        print(max_num)
    else:
        heapq.heappush(heap, (-input_num, input_num))

