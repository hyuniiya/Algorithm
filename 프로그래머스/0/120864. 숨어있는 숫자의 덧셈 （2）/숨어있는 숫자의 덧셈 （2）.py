def solution(my_string):
    total = 0
    current_number = ''
    
    for char in my_string:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                total += int(current_number)
                current_number = ''
    
    if current_number:
        total += int(current_number)
    
    return total