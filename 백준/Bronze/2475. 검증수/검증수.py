numbers = list(map(int, input().split()))

sum_squares = sum(x**2 for x in numbers)

verification = sum_squares % 10

print(verification)