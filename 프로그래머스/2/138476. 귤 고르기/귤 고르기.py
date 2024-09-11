from collections import Counter


def solution(k, tangerine):
    answer = 0
    size_counts = Counter(tangerine)

    for size, count in size_counts.most_common():
        answer += 1
        k -= count
        if k <= 0:
            break

    return answer