N = int(input())

# 첫 번째 줄부터 N번째 줄까지 출력합니다.
for i in range(1, N + 1):
    stars = '*' * i
    spaces = ' ' * (2 * (N - i))
    print(stars + spaces + stars)

# N+1번째 줄부터 2N-1번째 줄까지 출력합니다.
for i in range(N - 1, 0, -1):
    stars = '*' * i
    spaces = ' ' * (2 * (N - i))
    print(stars + spaces + stars)