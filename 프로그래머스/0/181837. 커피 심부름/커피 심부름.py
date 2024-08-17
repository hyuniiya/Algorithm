def solution(order):
    americano_price = 4500
    cafelatte_price = 5000
    
    total_price = 0
    
    for drink in order:
        if "americano" in drink:
            total_price += americano_price
        elif "cafelatte" in drink:
            total_price += cafelatte_price
        elif drink == "anything":
            total_price += americano_price
    
    return total_price