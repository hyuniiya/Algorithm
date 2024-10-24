def solution(my_string):
    result = int(my_string.split()[0])
    
    for i in range(1, len(my_string.split()), 2):
        operator = my_string.split()[i]
        number = int(my_string.split()[i+1])
        
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
            
    return result