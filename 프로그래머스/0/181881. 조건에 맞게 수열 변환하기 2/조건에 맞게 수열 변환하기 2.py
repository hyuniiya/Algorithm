def solution(arr):
    x = 0
    while True:
        previous = arr[:]

        arr = [
            num // 2 if num >= 50 and num % 2 == 0 else 
            (num * 2) + 1 if num < 50 and num % 2 == 1 else 
            num
            for num in arr
        ]
        
        if previous == arr:
            break
        
        x += 1

    return x
