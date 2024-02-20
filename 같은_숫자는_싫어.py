def solution(arr):
    result = []
    length = len(arr)
    for index, number in enumerate(arr):
        if (index != length - 1 and number != arr[index + 1]) or index == length - 1:
            result.append(number)
    return result
