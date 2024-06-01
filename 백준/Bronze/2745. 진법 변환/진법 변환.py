def base_to_num():
    num, base = input().split()
    arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = 0
    # for 문에서 i=0 부터 시작이니 문자열을 뒤집어서 처리 해주기
    num = num[::-1]
    
    for i, digit in enumerate(num):
        result += int(base) ** i * arr.index(digit)
    print(result)

base_to_num()