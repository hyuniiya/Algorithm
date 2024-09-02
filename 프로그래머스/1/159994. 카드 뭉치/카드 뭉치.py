def solution(cards1, cards2, goal):
    cards1.append(0)
    cards2.append(0)
    for i in goal :
        if i == cards1[0]:
            cards1.remove(i)
        elif i == cards2[0]:
            cards2.remove(i)
        else :
            return "No"
            break

    return "Yes"