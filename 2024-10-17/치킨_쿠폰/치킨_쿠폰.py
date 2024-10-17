def solution(chicken):
    total_service = 0
    coupon = chicken
    while coupon >= 10:
        service = coupon // 10
        total_service += service
        coupon = coupon % 10 + service
    return total_service
