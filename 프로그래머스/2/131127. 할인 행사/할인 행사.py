def solution(want, number, discount):
    def check(b):
        for idx, w in enumerate(want):
            if b.count(w) < number[idx]: return False
        return True

    basket, days = discount.copy(), 0
    for idx, d in enumerate(discount):
        if check(basket[idx:idx+10]): days+=1
    return days