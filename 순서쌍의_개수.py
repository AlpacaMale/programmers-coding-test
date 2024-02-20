def solution(n):
    result = []
    for number in range(1, n + 1):
        if not n % number:
            result.append(number)
    return len(result)
