def solution(arr):
    row = len(arr)
    column = len(arr[0])
    if row > column:
        for array in arr:
            array.extend([0] * (row - column))
    elif column > row:
        arr.extend([[0] * column for _ in range(column - row)])
    return arr
