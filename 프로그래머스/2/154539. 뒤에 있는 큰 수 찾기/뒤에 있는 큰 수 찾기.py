def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    
    for i in range(len(numbers)):
        # 큰 값을 갖는 원소를 만날 때까지 순회
        while stack and numbers[stack[-1]] < numbers[i]:
            # 스택에 pop, 배열 갱신
            result[stack.pop()] = numbers[i]
        # 인덱스를 추가하여 비교
        stack.append(i)
        
    return result