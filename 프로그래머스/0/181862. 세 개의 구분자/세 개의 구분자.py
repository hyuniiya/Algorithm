def solution(myStr):
    answer = []
    current = ""
    
    for char in myStr:
         if char in ['a', 'b', 'c']:
                if current:
                    answer.append(current)
                    current = ""
         else:
            current += char
    if current:
        answer.append(current)
        
    return ["EMPTY"] if not answer else answer