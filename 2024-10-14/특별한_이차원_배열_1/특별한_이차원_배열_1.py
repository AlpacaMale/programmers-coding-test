def solution(n):
    arr = [[0] * n for _ in range(n)]
    for index in range(n):
        arr[index][index] = 1
    return arr
