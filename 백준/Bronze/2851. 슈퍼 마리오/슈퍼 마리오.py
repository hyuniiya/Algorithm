def close_number():
    mushrooms = []
    for i in range(10):
        mushrooms.append(int(input()))

    current_sum = 0
    best_score = 0

    for score in mushrooms:
        current_sum += score
        # 현재 점수가 100에 가까운지 확인
        if abs(100 - current_sum) < abs(100 - best_score):
            best_score = current_sum
        elif abs(100 - current_sum) == abs(100 - best_score):
            best_score = max(best_score, current_sum)

    print(best_score)

close_number()