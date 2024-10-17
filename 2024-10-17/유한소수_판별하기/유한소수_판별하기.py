from collections import Counter


def find_divisors(number):
    divisors = []
    current = 2
    while number != 1:
        if number % current == 0:
            number //= current
            divisors.append(current)
        else:
            current += 1
    return Counter(divisors)


def solution(a, b):
    divisor_a = find_divisors(a)
    divisor_b = find_divisors(b)
    return (
        1
        if all(
            divisor == 2 or divisor == 5
            for divisor in (divisor_b - divisor_a).elements()
        )
        else 2
    )
