def solution(numbers):
    word_to_num = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    result = ""
    current_word = ""
    for char in numbers:
        current_word += char
        if current_word in word_to_num:
            result += word_to_num[current_word]
            current_word = ""
    
    if current_word:
        result += word_to_num[current_word]
    
    return int(result)