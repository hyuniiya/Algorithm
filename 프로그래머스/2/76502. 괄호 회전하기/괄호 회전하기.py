def is_valid(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0

def solution(s):
    count = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1
    return count