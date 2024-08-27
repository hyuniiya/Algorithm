from itertools import combinations

def solution(numbers):
    pick_two_number_list = combinations(numbers, 2)
    sums = []

    for pair in pick_two_number_list:
        sums.append(sum(pair))

    return sorted(set(sums))