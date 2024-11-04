def solution(n):
    count = 0 
    for start in range(1, n + 1): 
        sum = 0 
        
        for num in range(start, n + 1):
            sum += num
            
            if sum == n:
                count += 1 
                break
            elif sum > n:
                break
    return count