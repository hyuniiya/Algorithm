def solution(word):
    answer = 0
    word_list = []
    words = "AEIOU"
    
    def all_word(length, w):
        if length == 5:
            return
        for i in range(len(words)):
                word_list.append(w + words[i])
                all_word(length + 1, w + words[i])
                
            
    all_word(0, "")
    
    return word_list.index(word) + 1