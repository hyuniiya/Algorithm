def solution(n, m, section):
    count = 0
    painted_until = 0
    
    for s in section:
        if s > painted_until:
            count += 1
            painted_until = s + m - 1
    
    return count