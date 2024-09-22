from collections import Counter

def solution(want, number, discount):
    target = Counter(dict(zip(want, number)))
    count = 0
    
    for i in range(len(discount) - 9):
        window = Counter(discount[i:i+10])
        if window == target:
            count += 1
    
    return count