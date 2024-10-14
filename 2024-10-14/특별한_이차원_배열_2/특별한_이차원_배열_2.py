def solution(arr):
    n = len(arr)
    for index in range(n):
        for _index in range(index + 1, n):
            if arr[index][_index] != arr[_index][index]:
                return 0
    return 1
