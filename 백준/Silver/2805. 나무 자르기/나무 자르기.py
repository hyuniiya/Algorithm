import sys
def cutter_maximum():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    heights = list(map(int, input().split()))

    # 이진 탐색을 위한 탐색 범위 설정
    low = 0
    high = max(heights)
    cutter_height = 0

    # 이진 탐색
    while low <= high:
        mid = (low + high) // 2  # 중간 높이 설정
        total = 0  # 잘린 나무 총 길이

        # 각 나무 높이 확인하며 잘린 나무 총 길이 계산
        for h in heights:
            if h > mid:
                total += h - mid

        # 잘린 나무의 총 길이가 필요한 나무의 길이보다 작으면 높이를 줄임
        if total < M:
            high = mid - 1
        # 잘린 나무의 총 길이가 필요한 나무의 길이보다 크거나 같으면 결과 갱신 후 높이를 늘림
        else:
            cutter_height = mid
            low = mid + 1

    print(cutter_height)
cutter_maximum()