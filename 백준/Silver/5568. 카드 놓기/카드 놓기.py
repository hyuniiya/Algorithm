from itertools import permutations

n = int(input())
k = int(input())
card_list = [input() for _ in range(n)]

# 가능한 모든 조합을 저장, 중복 제거
all_combinations = set()

# permutations 함수를 사용하여 순열 생성
for perm in permutations(card_list, k):
    all_combinations.add(''.join(perm))

# 결과 출력
print(len(all_combinations))