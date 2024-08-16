def solution(s):
    words = s.split(' ')  # 공백 기준으로 단어를 나눔
    
    result = []
    
    for word in words:
        transformed_word = ''
        for i in range(len(word)):
            if i % 2 == 0:  # 짝수 인덱스 -> 대문자
                transformed_word += word[i].upper()
            else:           # 홀수 인덱스 -> 소문자
                transformed_word += word[i].lower()
        result.append(transformed_word)
    
    return ' '.join(result)