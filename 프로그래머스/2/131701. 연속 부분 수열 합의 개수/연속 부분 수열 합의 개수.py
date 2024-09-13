from collections import deque

def solution(elements):
    n = len(elements)
    result = set()
    
    dq = deque(elements)
    
    for _ in range(n):
        current_sum = 0
        for i in range(n):
            current_sum += dq[i]
            result.add(current_sum)
        
        dq.rotate(-1)
    
    return len(result)