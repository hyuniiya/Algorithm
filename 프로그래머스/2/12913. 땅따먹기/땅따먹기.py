def solution(land):
    for row in range(1, len(land)):
        prev_row = land[row-1]
        curr_row = land[row]
        
        for col in range(4):
            other_cols = [] 
            for i in range(4): 
                if i != col:
                    other_cols.append(prev_row[i])
            curr_row[col] += max(other_cols)

    return max(land[-1])