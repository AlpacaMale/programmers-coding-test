from collections import Counter


def solution(array):
    array_count = Counter(array)
    max_freq = max(array_count.values())
    most_common = [key for key, count in array_count.items() if count == max_freq]
    return most_common[0] if len(most_common) == 1 else -1
