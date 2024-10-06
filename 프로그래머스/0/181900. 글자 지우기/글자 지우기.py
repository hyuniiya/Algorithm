def solution(my_string, indices):
    indices.sort(reverse=True)
    
    my_string = list(my_string)
    for i in indices:
        del my_string[i]
    return ''.join(my_string)