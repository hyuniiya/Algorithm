def degree():
    n = int(input())
    sum = 0
    for i in range(1, n):  # 1부터 n-1까지 반복
        sum += (n - i)  # 각 i에 대해 (n - i)번 수행
    
    print(sum)
    print(2)

degree()