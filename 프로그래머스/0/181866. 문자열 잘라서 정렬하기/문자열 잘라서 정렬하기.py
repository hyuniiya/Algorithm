def solution(myString):
    split_array = myString.split("x")
    
    non_empty_array = []
    for item in split_array:
        if item != "":
            non_empty_array.append(item)
    
    sorted_array = sorted(non_empty_array)
    
    return sorted_array