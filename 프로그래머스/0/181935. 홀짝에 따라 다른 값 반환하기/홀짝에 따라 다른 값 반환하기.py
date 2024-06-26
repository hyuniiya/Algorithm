def solution(n):
    if n % 2 == 1:  # n이 홀수인 경우
        sum_odd = (n // 2 + 1) ** 2
        return sum_odd
    else:  # n이 짝수인 경우
        sum_even_squares = 0
        for i in range(2, n + 1, 2):
            sum_even_squares += i ** 2
        return sum_even_squares