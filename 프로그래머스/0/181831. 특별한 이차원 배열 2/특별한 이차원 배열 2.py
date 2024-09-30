def solution(arr):
    n = len(arr)
    
    for i in range(1, n):
        for j in range(i):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1