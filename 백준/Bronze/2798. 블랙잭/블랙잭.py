# 카드 3장의 모든 조합 탐색하고, 각 조합의 합 구하기
# 합이 target_sum을 넘지 않으면서 가까운 최대합 찾기
import sys
from itertools import combinations

def blackjack():
    input = sys.stdin.readline
    num_cards , target_sum = map(int, input().split())
    card_list = list(map(int, input().split()))

    max_sum = 0
    for card_combo in combinations(card_list, 3):
        current_sum = sum(card_combo)
        if current_sum <= target_sum and current_sum > max_sum:
            max_sum = current_sum
    print(max_sum)

blackjack()