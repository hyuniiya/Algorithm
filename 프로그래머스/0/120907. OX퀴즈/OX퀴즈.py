def solution(quiz):
    result = []
    
    for expression in quiz:
        parts = expression.split()
        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])
        answer = int(parts[4])
        calculated = num1 + num2 if operator == '+' else num1 - num2
        result.append("O" if calculated == answer else "X")
    
    return result