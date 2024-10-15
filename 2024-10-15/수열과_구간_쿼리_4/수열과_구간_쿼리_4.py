def solution(arr, queries):
    for [s, e, k] in queries:
        start = s if s % k == 0 else s + (k - s % k)
        end = e + 1
        for index in range(start, end, k):
            arr[index] += 1
    return arr


# 시작지점은 k의 배수이며,
# s보다 start가 더크거나 같아야한다.
