def solution(arr):
    stk = []
    for element in arr:
        if not stk or stk[-1] != element:
            stk.append(element)
        else:
            stk.pop()
    return stk or [-1]
