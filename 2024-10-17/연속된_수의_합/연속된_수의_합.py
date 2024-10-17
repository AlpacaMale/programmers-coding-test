def solution(num, total):
    start = (total // num) - (num // 2) + int(num % 2 == 0)
    end = (total // num) + (num // 2) + 1
    return list(range(start, end))
