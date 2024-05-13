from collections import Counter

def solution(topping):
    answer = 0
    left_cnt = Counter()
    right_cnt = Counter(topping)
    
    for topp in topping:
        left_cnt[topp] += 1
        right_cnt[topp] -= 1
        
        if right_cnt[topp] == 0:
            del right_cnt[topp]
        
        if len(left_cnt) == len(right_cnt):
            answer += 1
        
        if len(left_cnt) > len(right_cnt):
            break
    
    return answer