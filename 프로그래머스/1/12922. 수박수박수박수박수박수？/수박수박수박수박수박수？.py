def solution(n):
    pattern = "수박" * (n // 2 + 1)
    result = pattern[:n]
    return result