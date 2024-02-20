def solution(absolutes, signs):
    result = 0
    for number, sign in zip(absolutes, signs):
        result += number if sign else -number
    return result
