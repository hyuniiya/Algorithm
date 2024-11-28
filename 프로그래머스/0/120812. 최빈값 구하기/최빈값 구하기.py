def solution(array):
    if not array:
        return None
    
    count_dict = {}
    for num in array:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_count = max(count_dict.values())
    
    most_frequent = [num for num, count in count_dict.items() if count == max_count]
    
    return most_frequent[0] if len(most_frequent) == 1 else -1