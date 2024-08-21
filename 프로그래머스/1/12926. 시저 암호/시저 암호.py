def solution(s, n):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    
    for char in range(len(s)): 
        if s[char] == ' ': 
            answer += ' '
        elif s[char].isupper():
            answer += upper[(upper.index(s[char]) + n) % 26]
        else:
            answer += lower[(lower.index(s[char]) + n) % 26]
    return answer