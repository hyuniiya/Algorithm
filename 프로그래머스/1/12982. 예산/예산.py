def solution(d, budget):
    d.sort()
    count = 0
    
    for req in d:
        if req <= budget:
            budget -= req
            count += 1
        else:
            break
    
    return count