import itertools

def prime(n):
    if n < 2:
        return 0
    else:
        for i in range(2,n):
            if n % i == 0: 
                return 0
        return 1
    
def solution(nums):
    answer = 0
    combi = list(itertools.combinations(nums,3))

    for i in range(len(combi)):
        answer += prime(sum(combi[i]))
    
    return answer