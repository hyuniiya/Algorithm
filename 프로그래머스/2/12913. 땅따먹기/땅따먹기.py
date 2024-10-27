def solution(land):
    for row in range(1, len(land)):
        prev_row = land[row-1]
        curr_row = land[row]
        
        for col in range(4):
            other_cols = [prev_row[i] for i in range(4) if i != col]
            curr_row[col] += max(other_cols)
    
    return max(land[-1])