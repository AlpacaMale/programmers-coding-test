def solution(n):
    count = 1
    number = 1
    while number != n:
        count += 1
        if "3" not in str(count) and count % 3 != 0:
            number += 1
    return count
