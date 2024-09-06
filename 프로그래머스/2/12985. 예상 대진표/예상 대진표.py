def solution(n, a, b):
    for answer in range(1, n):
        a = (a + 1) // 2
        b = (b + 1) // 2
        if a == b:
            return answer

    return answer