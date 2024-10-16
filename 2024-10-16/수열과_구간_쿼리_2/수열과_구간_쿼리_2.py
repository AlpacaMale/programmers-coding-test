def solution(arr, queries):
    result = []
    for [s, e, k] in queries:
        tmp = [number for number in arr[s : e + 1] if number > k]
        result.append(min(tmp) if tmp else -1)
    return result
