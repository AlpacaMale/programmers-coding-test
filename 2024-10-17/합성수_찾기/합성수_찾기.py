import math


def solution(n):
    total_composite = 0

    for num in range(1, n + 1):
        divisor_count = 1
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisor_count += 1
        if divisor_count >= 3:
            total_composite += 1

    return total_composite
