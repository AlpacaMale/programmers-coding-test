def solution(ineq, eq, n, m):
    if eq == "=":
        flag = n >= m if ineq == ">" else n <= m
    else:
        flag = n > m if ineq == ">" else n < m
    return 1 if flag else 0
