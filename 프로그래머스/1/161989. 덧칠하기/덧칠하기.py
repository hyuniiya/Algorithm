def solution(n, m, section):
    intervals = []
    for s in section:
        if not intervals or s > intervals[-1][1]:
            intervals.append([s, s])
        else:
            intervals[-1][1] = s
    
    count = 0
    painted_until = 0
    for start, end in intervals:
        if start > painted_until:
            count += 1
            painted_until = start + m - 1
    
    return count