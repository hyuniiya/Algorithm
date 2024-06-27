def solution(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    
    # 두 결과를 비교하여 더 큰 값을 반환
    if ab > ba:
        return int(ab)
    else:
        return int(ba)