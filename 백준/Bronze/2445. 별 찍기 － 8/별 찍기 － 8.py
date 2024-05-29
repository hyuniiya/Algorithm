n = int(input())

for i in range(1, n+1):  # 1부터 n까지 증가
    print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)

for j in range(n-1, 0, -1):  # n-1부터 1까지 감소
    print("*"*j+" "*(n-j)+" "*(n-j)+"*"*j)