def solution(n):
    r, a, b = 1, n, 6
    while r != 0:
        r = a % b
        a, b = b, r
    return n / a
