def solution(my_string, m, c):
    result = ''

    for i in range(len(my_string) // m):
        result += my_string[i * m + (c - 1)]
    return result
