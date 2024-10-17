def solution(n):
    counter = 1
    for number in range(1, n // 2 + 1):
        if n % number == 0:
            counter += 1
    return counter
