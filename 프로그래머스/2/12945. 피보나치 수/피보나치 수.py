def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    mod = 1234567
    previous = 0
    current = 1
    
    for _ in range(2, n + 1):
        new_value = (previous + current) % mod
        previous = current
        current = new_value
    
    return current