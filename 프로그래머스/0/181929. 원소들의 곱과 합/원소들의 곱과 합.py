def solution(num_list):
    product = 1
    sum_value = 0
    
    for num in num_list:
        product *= num
        sum_value += num
    
    sum_square = sum_value ** 2
    
    if product < sum_square:
        return 1
    else:
        return 0