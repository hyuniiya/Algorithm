def solution(num_list):
    even_num = ''
    odd_num = ''
    
    for num in num_list:
        if num % 2 == 0:
            even_num += str(num)
        else:
            odd_num += str(num)
    
    # 문자열을 정수로 변환하여 합산
    return int(even_num) + int(odd_num)