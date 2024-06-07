from itertools import combinations

def find_seven():
    heights = []

    for i in range(9):
        height = int(input())
        heights.append(height)

    # 9개 중에 7개를 선택하는 모든 조합 리스트로 만들기
    seven_combinations = list(combinations(heights, 7))

    # 합이 100이 되는 조합 찾기
    for combo in seven_combinations:
        if sum(combo) == 100:
            answer = list(combo)  # 합이 100이면, 리스트로 저장하기
            break
    # 오름차순으로 정렬하기
    answer.sort()

    for height in answer:
        print(height)

find_seven()