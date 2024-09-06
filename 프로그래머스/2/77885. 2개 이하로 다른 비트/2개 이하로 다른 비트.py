def solution(numbers):
    def next_number(x):
        if x & 1 == 0:  # 짝수인 경우
            return x + 1
        
        # 연속된 1의 패턴 찾기
        c = x & -x
        r = x + c
        return (((r ^ x) >> 2) // c) | r

    return [next_number(num) for num in numbers]