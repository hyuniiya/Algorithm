def solution(l, r):
    result = []
    for num in range(l, r + 1):
        if all(char in "05" for char in str(num)):
            result.append(num)
    return result if result else [-1]