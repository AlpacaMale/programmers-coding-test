def solution(n):
    if n % 2 == 1:
        return sum(range(1, n + 1, 2))
    else:
        return sum(number**2 for number in range(0, n + 1, 2))
