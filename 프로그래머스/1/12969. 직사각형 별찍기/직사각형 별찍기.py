n, m = map(int, input().split())

# 세로로 m번 반복
for _ in range(m):
    # 가로로 n개의 별을 출력
    print('*' * n)