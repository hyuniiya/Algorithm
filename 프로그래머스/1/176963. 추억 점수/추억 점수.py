from collections import defaultdict

def solution(name, yearning, photo):
    # defaultdict을 사용하여 이름과 그리움 점수를 매핑
    yearning_dict = defaultdict(int, {name[i]: yearning[i] for i in range(len(name))})
    
    # 각 사진별로 추억 점수를 계산하여 리스트에 저장
    result = [sum(yearning_dict[person] for person in pic) for pic in photo]
    
    return result