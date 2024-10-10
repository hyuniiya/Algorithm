def solution(intStrs, k, s, l):
    result = []
    for string in intStrs:
        substring = string[s:s+l]
        number = int(substring)
        if number > k:
            result.append(number)
    return result