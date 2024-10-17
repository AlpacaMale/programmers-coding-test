def solution(n, k):
    free_drinks = n // 10
    return 12000 * n + 2000 * (k - free_drinks)
