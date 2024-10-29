def solution(chicken):
    service_chickens = 0
    coupons = chicken

    while coupons >= 10:
        new_service = coupons // 10
        service_chickens += new_service
        coupons = coupons % 10 + new_service

    return service_chickens