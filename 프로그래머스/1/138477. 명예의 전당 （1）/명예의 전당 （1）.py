def solution(k, score):
    honor_list = []
    result = []
    
    for s in score:
        if len(honor_list) < k:
            honor_list.append(s)
        else:
            if s > min(honor_list):
                honor_list.remove(min(honor_list))
                honor_list.append(s)
        
        result.append(min(honor_list))
    
    return result