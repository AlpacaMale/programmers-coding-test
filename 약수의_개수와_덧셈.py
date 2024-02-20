def solution(left, right):
    result = 0
    for number in range(left, right + 1):
        yaksu = len([x for x in range(1, number + 1) if not number % x])
        result += number if yaksu % 2 == 0 else -number
    return result
