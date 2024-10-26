def repeat_string():
    input_str = input().split()
    s = input_str[0] 
    n = int(input_str[1]) 

    result = s * n
    print(result)

repeat_string()
