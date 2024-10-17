def get_slope(a, b):
    return abs(a[1] - b[1]) / abs(a[0] - b[0])


def solution(dots):
    a, b, c, d = dots
    if (
        get_slope(a, b) == get_slope(c, d)
        or get_slope(a, c) == get_slope(b, d)
        or get_slope(a, d) == get_slope(b, c)
    ):
        return 1
    return 0
