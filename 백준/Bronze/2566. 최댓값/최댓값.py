def maximum_value():
    # 9x9 격자판 → 2차원 리스트로 변환
    grid = [
        list(map(int, input().split()))
        for _ in range(9)
    ]
    # 1차원 리스트에 행,열 순회하며 하나씩 추가하기
    flat_grid = [num for row in grid for num in row]

    # 최댓값과 최댓값의 인덱스 구하기
    max_value = max(flat_grid)
    max_index = flat_grid.index(max_value)

    # 최댓값의 인덱스를 격자판의 형태로 변환하여 위치 구하기
    max_row = max_index // 9 + 1
    max_col = max_index % 9 + 1

    print(max_value)
    print(max_row, max_col)

maximum_value()