import math
def star_count():
    n = int(input())
    count = math.factorial(n) // (math.factorial(n - 5) * math.factorial(5))
    print(count)
star_count()