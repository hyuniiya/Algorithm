def solution(myString, pat):
    transformed = myString.maketrans("AB", "BA")
    transformed_string = myString.translate(transformed)
    
    if pat in transformed_string:
        return 1
    else:
        return 0