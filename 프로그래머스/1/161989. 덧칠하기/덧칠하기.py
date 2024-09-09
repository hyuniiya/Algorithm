def solution(n, m, section):
    count = 0
    current_position = 0
    
    for s in section:
        if s > current_position:
            count += 1
            current_position = s + m - 1
            
    return count