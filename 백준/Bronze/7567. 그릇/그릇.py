def plate():
    n = input()
    # 그릇 높이 10으로 시작
    start = 10
    # 문자열 순회하며 같은 문자면 +5, 다른 문자면 +10
    for i in range(1,len(n)):
        if n[i] == n[i-1]:
            start += 5
        else:
            start += 10
    return start

print(plate())