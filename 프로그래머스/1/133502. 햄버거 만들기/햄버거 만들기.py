def solution(ingredient):
    pattern = [1, 2, 3, 1]
    answer = 0
    stack = []
    
    for item in ingredient:
        stack.append(item)
        
        if len(stack) >= len(pattern):
            if stack[-len(pattern):] == pattern:
                del stack[-len(pattern):]
                answer += 1
    
    return answer