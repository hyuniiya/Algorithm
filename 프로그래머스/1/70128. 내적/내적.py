def solution(a, b):
    result = 0
    
    # a와 b의 길이가 동일 > a 길이만큼 반복
    for i in range(len(a)):
        result += a[i] * b[i]
    
    return result