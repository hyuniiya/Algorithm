def solution(my_string, queries):
    chars = list(my_string)
    
    for s, e in queries:
        chars[s:e+1] = chars[s:e+1][::-1]
    
    return ''.join(chars)