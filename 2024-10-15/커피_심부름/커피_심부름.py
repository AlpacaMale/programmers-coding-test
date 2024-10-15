def solution(orders):
    total_price = 0
    for order in orders:
        total_price += 5000 if "latte" in order else 4500
    return total_price
