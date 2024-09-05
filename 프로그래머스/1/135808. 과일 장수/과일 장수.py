def solution(k, m, score):
    score.sort()
    
    total_profit = 0

    for start_index in range(len(score) - m, -1, -m):
        total_profit += score[start_index] * m
    
    return total_profit