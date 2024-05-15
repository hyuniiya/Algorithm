def solution(sequence, k):
    answer = []
    
    li = list()
    
    start = 0
    end = 0
    result = sequence[end]
    while (start < len(sequence)) and (end < len(sequence)):
        if (result < k):
            end += 1
            if (end < len(sequence)):
                result += sequence[end]
            
        else:
            if (result == k):
                li.append([start, end])

            result -= sequence[start]
            start += 1
        
    li.sort(key = lambda x : x[1] - x[0])
    answer = li[0]
    
    return answer