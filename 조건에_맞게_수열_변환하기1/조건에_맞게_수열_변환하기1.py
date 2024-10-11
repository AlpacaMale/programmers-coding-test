def solution(arr):
    for index in range(len(arr)):
        if arr[index] >= 50 and not arr[index] % 2:
            arr[index] /= 2
        elif arr[index] < 50 and arr[index] % 2:
            arr[index] *= 2
    return arr
