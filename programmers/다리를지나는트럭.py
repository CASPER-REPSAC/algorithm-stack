bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

answer = 0
bridge = []
trucks = [[w, bridge_length] for w in truck_weights]

while trucks or bridge:
    for i in bridge:
        i[1] -= 1
    bridge = [i for i in bridge if i[1] != 0]
    answer += 1

    if trucks:
        if (len(bridge) <= bridge_length) and sum(i[0] for i in bridge) + trucks[0][0] <= weight:
            bridge.append(trucks.pop(0))
    print(answer, bridge, end=' / ')
    print(trucks)

print(answer)