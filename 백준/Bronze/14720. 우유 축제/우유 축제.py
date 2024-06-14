def max_milk():
    n = int(input())
    market = list(map(int, input().split()))

    max_count = 0

    for i in range(n):
        if market[i] == max_count % 3:
            max_count += 1
    return max_count
print(max_milk())