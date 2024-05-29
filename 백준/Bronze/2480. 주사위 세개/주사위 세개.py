from collections import Counter

num_list = list(map(int, input().split())) # [1,1,2]
count = Counter(num_list)  # {2:1, 1:2}
most_common = count.most_common(1) # 빈도가 가장 높은 요소를 담은 리스트를 반환

if most_common[0][1] == 3:
    prize = 10000 + most_common[0][0] * 1000
elif most_common[0][1] == 2:
    prize = 1000 + most_common[0][0] * 100
else:
    prize = max(num_list) * 100

print(prize)