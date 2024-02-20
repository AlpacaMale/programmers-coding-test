def solution(n, m):
    a, b = n, m
    while b != 0:
        r = a % b
        a, b = b, r
    return [a, n * m / a]
