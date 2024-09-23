from collections import Counter

def solution(want, number, discount):
    target = Counter(dict(zip(want, number)))
    days = 0
    
    for i in range(len(discount) - 9):
        current = Counter(discount[i:i+10])
        if current == target:
            days += 1
    
    return days