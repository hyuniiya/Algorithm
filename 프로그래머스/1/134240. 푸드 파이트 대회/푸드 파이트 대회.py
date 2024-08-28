def solution(food):
    left_side = ''

    for food_type in range(1, len(food)):
        portion = food[food_type] // 2
        left_side += str(food_type) * portion
    
    result = left_side + "0" + left_side[::-1]
    
    return result