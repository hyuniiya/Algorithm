# 문자열 수열 -> 정수로 변환
import sys,string

# 문자열의 길이
input = sys.stdin.readline
L = int(input())
# 문자열
string_input = input()
r = 31
M = 1234567891

# 최종 해시 값 저장
answer = 0

# 각 문자의 값을 계산
for i in range(L):
    # 현재 문자의 값 위치 변환
    value = string.ascii_lowercase.index(string_input[i]) + 1
    answer += value * (r ** i)

print(answer % M)