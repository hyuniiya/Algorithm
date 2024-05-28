from itertools import combinations

def solution(number):
    count = 0
    # 3개의 숫자 조합
    for comb in combinations(number, 3):
        if sum(comb) == 0:
            count += 1
    return count