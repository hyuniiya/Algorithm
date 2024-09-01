def solution(number):
    total = 0
    for digit in number:
        total += int(digit)
        total %= 9
        
    return total