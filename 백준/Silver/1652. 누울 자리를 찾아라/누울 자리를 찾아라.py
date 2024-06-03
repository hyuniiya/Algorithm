# 각 행과 열에서 연속된 빈 공간 찾기
# 가로에 연속된 빈공간 찾기
# 세로에 연속된 빈공간 찾기
def find_room():
    n = int(input())
    # ['....X', '..XX.', '.....', '.XX..', 'X....']
    room = [input() for _ in range(n)]

    # 가로로 연속된 빈공간 찾기
    horizontal_count = 0
    for row in room:
        empty_spaces = row.split('X')
        for space in empty_spaces:
            if len(space) >= 2:
                horizontal_count += 1

    # 세로로 연속된 빈공간 찾기
    vertical_count = 0
    for j in range(n):
        column = ''.join(room[i][j] for i in range(n))
        empty_spaces = column.split('X')
        for space in empty_spaces:
            if len(space) >= 2:
                vertical_count += 1

    print(horizontal_count, vertical_count)


find_room()