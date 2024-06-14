def change_count():
    n = int(input())
    coins = [500, 100, 50, 10, 5, 1]
    change = 1000 - n

    count = 0
    for coin in coins:
        if change == 0:
            break
            
        count += change // coin
        change %= coin

    return count

print(change_count())