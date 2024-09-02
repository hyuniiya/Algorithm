def solution(k, score):
    answer = []
    rank = []
    
    for i in score:
        rank.append(i)
        rank = sorted(rank,reverse=True)
        
        if len(rank) > k:
            rank.pop()
        answer.append(rank[-1])
        
    return answer