import math

def solution(n,a,b):
    round = 0
    while a != b:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        round += 1
    return round