def solution(arr, k):
    new_arr = []
    for number in arr:
        if number not in new_arr:
            new_arr.append(number)
            if len(new_arr) == k:
                return new_arr
    return new_arr + [-1] * (k - len(new_arr))
