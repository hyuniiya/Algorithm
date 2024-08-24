def solution(numLog):
    result = []
    for i, num in enumerate(numLog[1:], start=1):
        diff = num - numLog[i - 1]
        if diff == 1:
            result.append('w')
        elif diff == -1:
            result.append('s')
        elif diff == 10:
            result.append('d')
        elif diff == -10:
            result.append('a')
    
    return ''.join(result)