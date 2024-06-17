import sys,itertools,math
def three_lcm(a,b,c):
    return math.lcm(a, b, c)
def solution():
    input = sys.stdin.readline
    num_list = list(map(int, input().split()))
    three_combinations_list = itertools.combinations(num_list, 3)

    lcm_values = []
    for combo in three_combinations_list:
        a, b, c = combo
        result = three_lcm(a, b, c)
        lcm_values.append(result)

    print(min(lcm_values))
solution()