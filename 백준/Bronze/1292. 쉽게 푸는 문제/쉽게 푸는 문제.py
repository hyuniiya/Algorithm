start_index, end_index = map(int, input().split())

# 수열 생성
number_sequence = []
current_value = 1

while len(number_sequence) < end_index:
    number_sequence.extend([current_value] * current_value)
    current_value += 1

# 구간의 합 계산
result = sum(number_sequence[start_index-1:end_index])
print(result)