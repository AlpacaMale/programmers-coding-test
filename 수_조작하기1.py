def solution(n, control):
    execute = {"w": 1, "s": -1, "d": 10, "a": -10}
    for key in control:
        n += execute[key]
    return n
