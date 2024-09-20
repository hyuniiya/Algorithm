def solution(arr1, arr2):
    answer = [] 

    for row in arr1:
        new_row = []
        for col in zip(*arr2):
            sum_value = 0 
            for a, b in zip(row, col):
                sum_value += a * b
            new_row.append(sum_value)
        answer.append(new_row)

    return answer