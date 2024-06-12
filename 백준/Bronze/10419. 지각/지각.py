def max_late_time():
    test_cases = int(input())  # 테스트 케이스 개수 입력

    for _ in range(test_cases):
        class_duration = int(input())  # 수업시간 입력

        late_time = 0  # 초기 지각 시간

        # 교수님이 지각하는 시간을 증가시키며 반복
        while True:
            total_time = late_time + late_time ** 2  # 총 수업시간 계산

            # 총 수업시간이 주어진 수업시간보다 크면 종료
            if total_time > class_duration:
                print(late_time - 1)
                break

            late_time += 1  # 지각 시간 증가
max_late_time()