def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = [0]*bridge_length
    while len(onBridge):
        answer += 1
        onBridge.pop(0)
        if truck_weights:
            if sum(onBridge)+truck_weights[0] <= weight:
                onBridge.append(truck_weights.pop(0))
            else:
                onBridge.append(0)
    return answer
