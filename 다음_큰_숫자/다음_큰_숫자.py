def solution(n):
    before_count = bin(n).count("1")
    after_count = 0
    while before_count != after_count:
        n += 1
        after_count = bin(n).count("1")
    return n
