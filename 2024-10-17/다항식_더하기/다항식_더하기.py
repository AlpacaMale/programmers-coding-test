def solution(polynomial):
    polynomial = polynomial.split(" + ")
    number = 0
    x = 0
    for term in polynomial:
        if term.isdigit():
            number += int(term)
        elif term == "x":
            x += 1
        else:
            x += int(term[:-1])
    prefix = (str(x) if x > 1 else "") + ("x" if x else "")
    suffix = str(number) if number else ""
    return prefix + (" + " if prefix and suffix else "") + suffix
