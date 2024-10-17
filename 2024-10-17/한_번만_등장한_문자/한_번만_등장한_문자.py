from collections import Counter


def solution(s):
    char_freq = Counter(s)
    return "".join(sorted(char for char in char_freq if char_freq[char] == 1))
