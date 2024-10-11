def solution(arr, k):
    if k % 2 == 0:
        return [number + k for number in arr]
    else:
        return [number * k for number in arr]
