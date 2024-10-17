def solution(n):
    pactorial = 1
    count = 1
    while pactorial <= n:
        count += 1
        pactorial *= count
    return count - 1
