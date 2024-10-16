def solution(l, r):
    start = 5 * (l // 5)
    end = 5 * (r // 5) + 1
    return [
        number
        for number in range(start, end, 5)
        if l <= number <= r and all(c in "05" for c in str(number))
    ] or [-1]
