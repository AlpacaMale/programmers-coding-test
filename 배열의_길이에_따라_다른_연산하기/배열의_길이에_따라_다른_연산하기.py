def solution(arr, n):
    flag = 1 if len(arr) % 2 == 1 else 0
    return [num if index % 2 == flag else num + n for index, num in enumerate(arr)]
