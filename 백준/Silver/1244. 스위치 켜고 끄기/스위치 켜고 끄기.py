def toggle_switches():
    n = int(input())  # 스위치 개수
    switches = list(map(int, input().split()))  # 스위치 상태
    students_count = int(input())  # 학생 수

    students = []
    for _ in range(students_count):
        gender, num = map(int, input().split())  # 각 학생의 성별과 받은 수 입력
        students.append((gender, num))

    # 스위치 상태 변경
    for gender, num in students:
        if gender == 1:
            for i in range(n):
                if (i + 1) % num == 0:  # 받은 수의 배수 위치인 경우
                    if switches[i] == 1:  # 현재 스위치 on일 경우
                        switches[i] = 0  # 스위치 off
                    else:
                        switches[i] = 1  # 스위치 on
        elif gender == 2:
            left = right = num - 1
            while left >= 0 and right < n and switches[left] == switches[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            for i in range(left, right + 1): # 대칭인 구간 내의 스위치 상태 변경
                switches[i] = 1 - switches[i]

    for i in range(0, n, 20):
        print(' '.join(map(str, switches[i:i+20])))

# 함수 호출
toggle_switches()