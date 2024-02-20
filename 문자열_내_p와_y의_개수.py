def solution(s):
    p, y = ["p", "P"], ["y", "Y"]
    result = 0
    for char in s:
        if char in p:
            result += 1
        elif char in y:
            result -= 1
    return result == 0
