def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {}
    for i in range(1, 27):
        dic[chr(i + 64)] = i
    
    answer = []
    w = ""
    index = 27
    
    for c in msg:
        wc = w + c
        if wc in dic:
            w = wc
        else:
            answer.append(dic[w])
            dic[wc] = index
            index += 1
            w = c
    
    if w:
        answer.append(dic[w])
    
    return answer