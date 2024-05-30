def solution():
    N = int(input())
    count = {}

    # 과일 종류, 개수 분리
    for i in range(N):
        S,X = input().split()
        fruit_count = int(X)
        # 과일 종류가 이미 존재할 경우, 과일 개수 추가
        if S in count:
            count[S] += fruit_count
        # 없을 경우, 과일 종류 추가
        else:
            count[S] = fruit_count
    # 5개인지 확인
    if 5 in count.values():
        print("YES")
    else:
        print("NO")

solution()