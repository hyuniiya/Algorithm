def solution(k, m, score):
    score.sort(reverse=True)
    
    total_profit = 0
    
    for i in range(0, len(score), m):
        if i + m > len(score):
            break
        p = score[i + m - 1]
        total_profit += p * m
    
    return total_profit