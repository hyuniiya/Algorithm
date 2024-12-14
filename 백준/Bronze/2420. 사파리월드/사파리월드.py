def solution(n, m):
    return abs(n - m)
n, m = map(int, input().split())

result = solution(n, m)
print(result)