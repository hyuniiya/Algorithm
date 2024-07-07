def solution(arr, delete_list):
    result = []

    for item in arr:
        if item not in delete_list:
            result.append(item)
    
    return result