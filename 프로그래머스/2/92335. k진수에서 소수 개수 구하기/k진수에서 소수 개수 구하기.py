# 10진수 -> k진수 변환(string)
def convert_to_k(n, k):
    num_str = ""
    
    while n > 0:
        n, r = divmod(n, k)
        num_str += str(r)
    
    return num_str[::-1]

# 소수인지 판단(boolean)
def is_prime(num):
    if num < 2:  
        return False
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0: 
            return False
    return True 

def solution(n, k):
    answer = 0 
    k_num = convert_to_k(n, k)  

#   0을 기준으로 분할하기(int)
    for n in k_num.split('0'):
        if n != "": 
            if is_prime(int(n)):
                answer += 1  
    
    return answer