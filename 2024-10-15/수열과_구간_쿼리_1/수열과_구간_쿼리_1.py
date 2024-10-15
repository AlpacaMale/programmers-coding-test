def solution(arr, queries):
    for s, e in queries:
        for index in range(s, e + 1):
            arr[index] += 1
    return arr
