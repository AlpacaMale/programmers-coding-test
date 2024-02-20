def solution(n):
    # x**y의 식으로 지수y를 표현할 수 있다
    return sum(range(1, n + 1, 2)) if n % 2 else sum(x**2 for x in range(2, n + 1, 2))
