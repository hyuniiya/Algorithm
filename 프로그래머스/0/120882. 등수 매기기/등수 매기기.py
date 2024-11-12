def solution(score):
    averages = [(sum(s) / 2, i) for i, s in enumerate(score)]
    
    sorted_averages = sorted(averages, key=lambda x: -x[0])
    
    ranks = [0] * len(score)
    current_rank = 1
    for i, (avg, original_index) in enumerate(sorted_averages):
        if i > 0 and sorted_averages[i][0] == sorted_averages[i - 1][0]:
            ranks[original_index] = ranks[sorted_averages[i - 1][1]]
        else:
            ranks[original_index] = current_rank
        current_rank += 1
    
    return ranks