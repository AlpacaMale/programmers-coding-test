def solution(order):
    return sum(1 for number in str(order) if number in "369")
