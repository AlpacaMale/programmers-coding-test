def solution(arr):
    length = len(arr)
    final_len = 1
    while length > final_len:
        final_len *= 2
    return arr + [0] * (final_len - length)
