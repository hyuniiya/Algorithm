def solution(s):
    stack = []
    
    for num in s.split():
        if num != 'Z':
            stack.append(int(num))
        else:
            if stack:
                stack.pop()
    
    return sum(stack)