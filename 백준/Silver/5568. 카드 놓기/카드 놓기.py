def backtrack(selected, used):
    if len(selected) == k:
        number = ''.join(selected)
        all_combinations.add(number)
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            selected.append(cards[i])
            backtrack(selected, used)
            selected.pop()
            used[i] = False


# 입력 받기
n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

# 가능한 모든 조합을 저장할 집합
all_combinations = set()

# 백트래킹 시작
backtrack([], [False] * n)

# 결과 출력
print(len(all_combinations))