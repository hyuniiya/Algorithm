def solution(polynomial):
    terms = polynomial.split(' + ')

    x_coefficient = 0
    constant = 0
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_coefficient += 1
            else:
                x_coefficient += int(term.replace('x', ''))
        else:
            constant += int(term)
    
    result = []
    
    if x_coefficient != 0:
        if x_coefficient == 1:
            result.append('x')
        else:
            result.append(f'{x_coefficient}x')
    
    if constant != 0:
        result.append(str(constant))
    
    return ' + '.join(result)