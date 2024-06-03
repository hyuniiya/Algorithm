def plus():
    N, M = map(int, input().split())

    def input_matrix(rows):
        return [list(map(int, input().split())) for _ in range(rows)]

    A = input_matrix(N)
    B = input_matrix(N)

    result = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]

    for row in result:
        print(" ".join(map(str, row)))

plus()