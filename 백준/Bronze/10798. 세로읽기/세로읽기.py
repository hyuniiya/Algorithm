from itertools import zip_longest

# 다섯 줄의 입력을 받습니다.
lines = [input().strip() for _ in range(5)]

# zip_longest를 사용하여 짧은 리스트들을 None으로 채워줍니다.
zipped = zip_longest(*lines, fillvalue='')

# 결과를 저장할 리스트를 초기화합니다.
result = []

# 병렬로 묶인 각 튜플에 대해 반복합니다.
for group in zipped:
    for char in group:
        if char:  # 빈 문자열이 아닌 경우에만 추가
            result.append(char)

# 결과 리스트를 문자열로 결합하여 출력합니다.
print("".join(result))