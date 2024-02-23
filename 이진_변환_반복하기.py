def solution(s):
    operations_count = 0
    removed_zeros_count = 0
    while s != "1":
        zeros_count = s.count("0")
        removed_zeros_count += zeros_count
        s_length = len(s) - zeros_count
        s = bin(s_length)[2:]
        operations_count += 1
    return [operations_count, removed_zeros_count]
