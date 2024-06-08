N = int(input())

# N부터 1까지 반복합니다.
for i in range(N):
    # 공백의 개수는 i개, 별의 개수는 N-i개입니다.
    spaces = ' ' * i
    stars = '*' * (N - i)
    # 공백과 별을 합쳐서 출력합니다.
    print(spaces + stars)