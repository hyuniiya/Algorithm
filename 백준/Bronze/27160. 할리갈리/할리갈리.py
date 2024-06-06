import sys
from collections import defaultdict

def ring_bell():
    input = sys.stdin.readline
    n = int(input())

    fruit_count = defaultdict(int) # {}

    for i in range(n):
        fruit, count = input().split() # ["BANANA" , "2", "PLUM", "4", "BANANA", "3"]
        fruit_count[fruit] += int(count) # {"BANANA": 5, "PLUM": 4}


    if  5 in fruit_count.values():
        print("YES")
    else:
        print("NO")
ring_bell()