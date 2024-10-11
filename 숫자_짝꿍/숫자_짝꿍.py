from collections import Counter


def solution(X, Y):
    intersection = Counter(X) & Counter(Y)
    result = ""
    for number, count in sorted(intersection.items(), reverse=True):
        if not result and number == "0":
            return "0"
        result += number * count
    return result or "-1"