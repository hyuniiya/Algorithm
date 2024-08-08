def solution(n):
    arr = []
    for i in range(n):
        row = [0] * n
        arr.append(row)
    
    for i in range(n):
        arr[i][i] = 1
    
    return arr