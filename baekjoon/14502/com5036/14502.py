import sys
from collections import deque
import copy


def bfs(lab_copy):
    visit = []
    queue = deque()
    for virus_pos in virus_list:
        y, x = virus_pos
        visit.append((y, x))
        queue.append((y, x))

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        # bfs로 virus를 퍼뜨림
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                y_ = y + dy[i]
                x_ = x + dx[i]

                if y_ < 0 or x_ < 0 or y_ >= n or x_ >= m:
                    continue

                # empty 공간에 virus 를 퍼뜨림
                if lab_copy[y_][x_] == 0 and (y_, x_) not in visit:
                    lab_copy[y_][x_] = 2
                    visit.append((y_, x_))
                    queue.append((y_, x_))

    # safe zone 세기
    count = 0
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 0:
                count += 1

    return count


lab = []
empty_list = []
virus_list = []

# 입력
n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    raw = list(map(int, sys.stdin.readline().split()))
    lab.append(raw)
    for j in range(m):
        if raw[j] == 0:
            empty_list.append((i, j))
        if raw[j] == 2:
            virus_list.append((i, j))

max_count = 0
for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            # 벽 세우기
            lab[y1][x1] = 1
            lab[y2][x2] = 1
            lab[y3][x3] = 1

            # 바이러스 퍼뜨리고 safe zone 수 반환
            count = bfs(copy.deepcopy(lab))
            # 최댓값으로 갱신
            max_count = max_count if max_count > count else count

            lab[y1][x1] = 0
            lab[y2][x2] = 0
            lab[y3][x3] = 0

print(max_count)
