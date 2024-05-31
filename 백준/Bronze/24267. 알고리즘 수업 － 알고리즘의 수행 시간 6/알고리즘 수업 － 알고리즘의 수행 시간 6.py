def degree():
    n = int(input())
    remain = n - 2
    total = 0

    for i in range(1, n-1):
        total += remain * i
        remain -= 1
    
    print(total, 3)

degree()