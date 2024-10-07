from collections import defaultdict

def solution(strArr):
    length_groups = defaultdict(int)

    for s in strArr:
        length_groups[len(s)] += 1
        
    return max(length_groups.values())