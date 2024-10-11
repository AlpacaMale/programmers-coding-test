def solution(n):
    result = 2
    while True:
        if n % result == 1:
            return result
        result += 1
