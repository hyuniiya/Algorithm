def solution(num_str):
    total_sum = 0
    
    for digit in num_str:
        num = int(digit)
        total_sum += num
    
    return total_sum
