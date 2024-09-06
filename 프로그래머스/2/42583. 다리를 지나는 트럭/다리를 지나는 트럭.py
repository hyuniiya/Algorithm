def solution(bridge_length, weight, truck_weights):
    bridge = []  # 다리를 건너는 트럭의 무게와 트럭의 위치를 저장하는 큐
    total_weight = 0  # 다리 위의 트럭의 무게를 저장할 변수 초기화
    time = 0  # 경과 시간을 저장할 변수 초기화

    # 모든 트럭이 큐에서 나올 때까지 반복
    while bridge or truck_weights:
        # 경과 시간을 1초 증가시킴
        time += 1

        # 큐에 있는 트럭들의 위치를 1씩 증가시킴
        for i in range(len(bridge)):
            bridge[i][1] += 1

        # 큐의 첫 번째 트럭이 다리 끝에 도달했다면
        if bridge and bridge[0][1] >= bridge_length:
            # 큐에서 제거하고 total_weight를 갱신함
            truck = bridge.pop(0)
            total_weight -= truck[0]

        # 대기 중인 트럭이 있고, 다리에 진입할 수 있다면
        if truck_weights and len(bridge) < bridge_length and total_weight + truck_weights[0] <= weight:
            # 큐에 트럭의 무게와 트럭의 위치를 추가하고 total_weight를 갱신함
            truck_weight = truck_weights.pop(0)
            bridge.append([truck_weight, 0])
            total_weight += truck_weight

    # 경과 시간을 반환함
    return time