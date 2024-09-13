def solution(elements):
    n = len(elements)

    extended = elements + elements
    
    sums = set()
    
    for start in range(n):
        for length in range(1, n + 1):
            sums.add(sum(extended[start:start + length]))
    
    return len(sums)