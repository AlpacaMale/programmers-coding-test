def solution(price):
    price_rate = 0
    if price >= 500000:
        price_rate = 20
    elif price < 500000 and price >= 300000:
        price_rate = 10
    elif price < 300000 and price >= 100000:
        price_rate = 5
    return price - (price * price_rate / 100)
