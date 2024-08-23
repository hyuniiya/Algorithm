from collections import Counter

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = Counter({1: 0, 2: 0, 3: 0})
    
    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            score[1] += 1
        if answer == pattern2[i % len(pattern2)]:
            score[2] += 1
        if answer == pattern3[i % len(pattern3)]:
            score[3] += 1
            
    max_score = max(score.values())
    
    result = []
    for i in range(3):
        if score[i + 1] == max_score:
            result.append(i + 1)
    
    print(result)
    return result