def solution(n):
    a = 1
    b = 1
    for num in range(2, n):
        a, b = a + b, a
    return a % 1234567
