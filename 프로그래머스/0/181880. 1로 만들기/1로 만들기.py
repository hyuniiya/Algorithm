def solution(num_list):
    answer = 0
    for num in num_list:
        operations = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (num - 1) // 2
            operations += 1
        answer += operations
    return answer