n = int(input())
num_list = list(map(int, input().split()))

dp = [1] * n # 각 원소가 그 자체로 길이 1인 부분 수열이므로 1로 초기화
for i in range(n):
    for j in range(i):
        if num_list[j] > num_list[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))