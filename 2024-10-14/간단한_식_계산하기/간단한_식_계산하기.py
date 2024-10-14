def solution(binomial):
    term1, operator, term2 = binomial.split()
    term1 = int(term1)
    term2 = int(term2)
    if operator == "+":
        return term1 + term2
    elif operator == "-":
        return term1 - term2
    else:
        return term1 * term2
