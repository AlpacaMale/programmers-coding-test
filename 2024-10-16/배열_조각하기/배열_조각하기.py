def solution(arr, queries):
    for index, query in enumerate(queries):
        arr = arr[: query + 1] if index % 2 == 0 else arr[query:]
    return arr
