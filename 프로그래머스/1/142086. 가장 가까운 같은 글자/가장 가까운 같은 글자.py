def solution(s):
    answer = []
    last_i = {}

    for current_i, char in enumerate(s):
        if char not in last_i:
            answer.append(-1)
        else:
            answer.append(current_i - last_i[char])
        last_i[char] = current_i
    return answer