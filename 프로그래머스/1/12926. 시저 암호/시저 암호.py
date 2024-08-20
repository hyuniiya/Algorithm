def solution(s, n):
    result = []
    
    for char in s:
        if char.isupper():  # 대문자 처리
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        elif char.islower():  # 소문자 처리
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:
            new_char = char  # 공백 처리
        result.append(new_char)
    
    return ''.join(result)