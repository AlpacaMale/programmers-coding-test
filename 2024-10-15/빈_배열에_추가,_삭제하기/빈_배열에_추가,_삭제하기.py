def solution(arr, flag):
    new_arr = []
    for number, is_true in zip(arr, flag):
        if is_true:
            new_arr.extend([number] * number * 2)
        else:
            del new_arr[-number:]
    return new_arr
