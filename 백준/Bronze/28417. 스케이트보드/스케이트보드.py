import sys

def find_max_final_score():
    input = sys.stdin.readline
    num_player = int(input())
    max_final_score = 0
    for i in range (num_player):
        score_list = list(map(int, input().split()))
        run_score_list = score_list[:2]
        trick_score_list = score_list[2:7]

        run_score_list.sort()
        trick_score_list.sort()

        sum_score = run_score_list[1] + trick_score_list[3] + trick_score_list[4]
        max_final_score = max(max_final_score, sum_score)


    print(max_final_score)
find_max_final_score()