def solution(emergency):
    result = []
    for i, current_emergency in enumerate(emergency):
        rank = 1
        for other_emergency in emergency:
            if other_emergency > current_emergency:
                rank += 1
        result.append(rank)
    return result