def solution(n, m, section):
    count = 0
    painted_until = 0
    index = 0
    
    while index < len(section):
        start = section[index]
        end = min(start + m - 1, n)
        count += 1
        
        while index < len(section) and section[index] <= end:
            index += 1
    
    return count