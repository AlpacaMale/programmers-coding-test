def solution(strArr):
    length_count = {}
    for string in strArr:
        length = len(string)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1
    return max(length_count.values())
