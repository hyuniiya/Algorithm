from collections import Counter

def solution(X, Y):
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    common = {}
    for digit in count_X:
        if digit in count_Y:
            common[digit] = min(count_X[digit], count_Y[digit])
    
    if not common:
        return "-1"
    
    result = []
    for digit in sorted(common.keys(), reverse=True):
        result.extend([digit] * common[digit])
    
    if all(digit == "0" for digit in result):
        return "0"
    
    return "".join(result)