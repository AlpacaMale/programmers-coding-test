def check_even(number):
    return number % 2 == 0


def solution(a, b):
    is_a_even = check_even(a)
    is_b_even = check_even(b)
    if not is_a_even and not is_b_even:
        return a**2 + b**2
    elif is_a_even ^ is_b_even:
        return 2 * (a + b)
    else:
        return abs(a - b)
