def solution(lines):
    line_count = [0] * 201
    
    for start, end in lines:
        for i in range(start + 100, end + 100):
            line_count[i] += 1
    
    overlapping_length = sum(1 for x in line_count if x > 1)
    
    return overlapping_length
