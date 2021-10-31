import sys

house_N, router_N = map(int, sys.stdin.readline().split())

houses_pos = [int(sys.stdin.readline()) for i in range(house_N)]
houses_pos.sort()

min_gap = 1
max_gap = houses_pos[-1] - houses_pos[0]

result = 0

while min_gap <= max_gap:
    mid = (min_gap + max_gap) // 2
    router_count = 1

    cur = houses_pos[0]
    for i in range(1, len(houses_pos)):
        if cur + mid <= houses_pos[i]:
            router_count += 1
            cur = houses_pos[i]

    if router_count < router_N:
        max_gap = mid - 1
    else:  # router_count >= router_N
        min_gap = mid + 1
        result = mid    # router_count == router_N 일 경우 간격을 늘리려다가 다음에 while 문이 종료 될 수도 있으므로 임시저장

print(result)
