def solution(n):
    return [number for number in range(1, n // 2 + 1) if n % number == 0] + [n]
