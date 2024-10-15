def solution(arr):
    if 2 not in arr:
        return [-1]
    start, end = 99999, 0
    for index, number in enumerate(arr):
        if number == 2:
            start = min(index, start)
            end = max(index + 1, end)
    return arr[start:end]
