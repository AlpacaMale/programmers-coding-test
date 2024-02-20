def solution(n):
    return sum(x for x in range(1,n+1) if not n%x)