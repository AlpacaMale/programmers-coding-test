def solution(num, k):
    k = str(k)
    for index, char in enumerate(str(num)):
        if char == k:
            return index + 1
    return -1
