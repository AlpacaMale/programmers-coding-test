def solution(arr):
    stk = []
    i = 0
    length = len(arr)
    while i < length:
        if not stk or arr[i] > stk[-1]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    return stk
