def solution(array, commands):
    answer = []
    for command in commands:
        start, end, target = command
        sliced_array = sorted(array[start-1:end])
        answer.append(sliced_array[target-1])

    return answer