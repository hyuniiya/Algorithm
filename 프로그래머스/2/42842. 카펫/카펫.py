def solution(brown, yellow):
    for height in range(1, int(yellow ** 0.5) + 1):
        if yellow % height == 0:
            width = yellow // height
            if brown == (width + 2) * 2 + height * 2:
                return [width + 2, height + 2]