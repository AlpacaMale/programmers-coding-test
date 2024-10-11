def solution(n):
    root_n = n**0.5
    return [-1, (root_n + 1) ** 2][root_n.is_integer()]
