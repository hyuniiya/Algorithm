def solution(before, after):
    if len(before) != len(after):
        return 0
    
    before_count = {}
    after_count = {}
    
    for char in before:
        before_count[char] = before_count.get(char, 0) + 1

    for char in after:
        after_count[char] = after_count.get(char, 0) + 1
    
    return 1 if before_count == after_count else 0