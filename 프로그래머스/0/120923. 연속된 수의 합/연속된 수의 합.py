def solution(num, total):
    start = (total - (num * (num - 1) // 2)) // num
    result = []
    for i in range(num):
        result.append(start + i)
    return result