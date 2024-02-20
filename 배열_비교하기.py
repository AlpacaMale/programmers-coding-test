def solution(arr1, arr2):
    arr1_length, arr2_length = len(arr1), len(arr2)
    if arr1_length > arr2_length:
        return 1
    elif arr1_length < arr2_length:
        return -1
    elif arr1_length == arr2_length and sum(arr1) > sum(arr2):
        return 1
    elif arr1_length == arr2_length and sum(arr1) < sum(arr2):
        return -1
    else:
        return 0
