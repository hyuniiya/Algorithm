import itertools
import math

# 소수 판별 함수 (제곱근까지만 확인)
def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    combi = itertools.combinations(nums, 3)
    prime_cache = {}  

    for comb in combi:
        if sum(comb) not in prime_cache:
            prime_cache[sum(comb)] = prime(sum(comb))
        answer += prime_cache[sum(comb)]
    
    return answer