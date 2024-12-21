def find_largest_label():
    N, L = map(int, input().split())
    
    count = 0
    num = 1
    
    while count < N:
        if str(L) not in str(num):
            count += 1
        num += 1
    
    return num - 1

print(find_largest_label())