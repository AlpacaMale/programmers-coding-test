def solution(arr, k):
    result = []
    for number in arr:
        new_element = number * k if k % 2 else number + k
        result.append(new_element)
    return result
