from itertools import permutations

def count_time_method():  # 시간을 세는 함수를 정의합니다.
    # 시간의 유효성을 검사하는 내부 함수를 정의합니다.
    def is_valid_hour(hh):  # 시간이 유효한지 검사하는 함수
        return 1 <= hh <= 12

    def is_valid_minute_or_second(mm_ss):  # 분 또는 초가 유효한지 검사하는 함수
        return 0 <= mm_ss < 60

    # 입력을 받고 시간을 시, 분, 초로 분리합니다.
    hh, mm, ss = map(int, input().split(':'))
    parts = [hh, mm, ss]  # 시, 분, 초를 리스트로 저장합니다.

    valid_combinations = 0  # 유효한 조합의 수를 저장할 변수를 초기화합니다.

    # 시, 분, 초의 모든 순열을 생성하고 유효성을 검사합니다.
    for perm in permutations(parts):
        hour, minute, second = perm  # 각 순열에서 시, 분, 초를 추출합니다.

        # 시간, 분, 초가 모두 유효한지 검사합니다.
        if is_valid_hour(hour) and is_valid_minute_or_second(minute) and is_valid_minute_or_second(second):
            valid_combinations += 1  # 유효한 조합의 수를 증가시킵니다.

    print(valid_combinations)  # 유효한 조합의 수를 출력합니다.

# 함수를 호출하여 실행합니다.
count_time_method()