def degree():
    n = int(input())
    sum = 0
    for i in range(1, n):  
        sum += (n - i)  
    
    print(sum, 2)

degree()