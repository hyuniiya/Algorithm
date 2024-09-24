def solution(clothes):
    cloth_type_count = {}
    
    for cloth, cloth_type in clothes:
        cloth_type_count[cloth_type] = cloth_type_count.get(cloth_type, 0) + 1
    
    answer = 1
    
    for count in cloth_type_count.values():
        answer *= (count + 1)
    
    return answer - 1