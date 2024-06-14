import sys

def max_target():
    input = sys.stdin.readline
    n = int(input())
    heights = list(map(int,input().split()))

    max_kills = 0
    kills = 0
    max_height = 0

    for height in heights:
        if height > max_height:
            kills = 0  # 더 높은 봉우리를 만나면 처치 수 초기화
            max_height = height  # 현재 높이를 최대 높이로 업데이트
        else:
            kills += 1  # 더 낮은 봉우리를 만나면 처치 수 증가
        max_kills = max(max_kills, kills)  # 최대 처치 수 갱신

    return max_kills

print(max_target())