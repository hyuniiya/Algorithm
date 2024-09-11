def is_valid_bracket_string(s):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    
    return len(stack) == 0

def solution(s):
    count = 0
    n = len(s)
    
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid_bracket_string(rotated):
            count += 1
    
    return count