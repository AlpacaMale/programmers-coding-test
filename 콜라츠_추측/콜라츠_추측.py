def solution(num):
    for attempt in range(501):
        if num == 1:
            return attempt
        num = num * 3 + 1 if num % 2 else num / 2
    return -1
