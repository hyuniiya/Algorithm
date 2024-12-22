while True:
    try:
        n, k = map(int, input().split())
        
        total = n
        stamps = n
        
        while stamps >= k:
            new_coupon = stamps // k
            stamps = stamps % k
            total += new_coupon
            stamps += new_coupon
            
        print(total)
        
    except:
        break