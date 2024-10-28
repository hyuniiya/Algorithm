def solution(numbers, k):
    current = 0
    
    for _ in range(k-1):
        current += 2
        if current >= len(numbers):
            current = current % len(numbers)
    
    return numbers[current]