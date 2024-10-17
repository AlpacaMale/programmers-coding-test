def solution(n):
    current = 2
    result = set()
    while n != 1:
        if n % current == 0:
            n //= current
            result.add(current)
        else:
            current += 1
    return sorted(result)
