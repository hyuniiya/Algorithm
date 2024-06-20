def solution(t, p):
    m = len(p)  # p의 길이
    p_num = int(p)  # p를 정수로 변환
    count = 0
    
    for i in range(len(t) - m + 1):
        substring = t[i:i + m]  # 길이가 m인 부분 문자열 추출
        if int(substring) <= p_num:  # 부분 문자열을 정수로 변환하여 비교
            count += 1  # 조건을 만족하면 카운트 증가
    
    return count