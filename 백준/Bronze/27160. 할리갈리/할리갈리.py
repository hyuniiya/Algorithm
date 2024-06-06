import sys
from collections import defaultdict

def ring_bell():
    n = int(sys.stdin.readline())

    fruit_count = defaultdict(int)

    for _ in range(n):
        fruit, count = sys.stdin.readline().split()
        fruit_count[fruit] += int(count)

    if 5 in fruit_count.values():
        print("YES")
    else:
        print("NO")

ring_bell()