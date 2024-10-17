def solution(arr):
    indices = [i for i, value in enumerate(arr) if value == 2]
    
    if not indices:
        return [-1]
    
    start_index = indices[0]
    end_index = indices[-1]

    return arr[start_index:end_index + 1]
