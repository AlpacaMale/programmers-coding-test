def solution(quiz):
    result = []
    for expression in quiz:
        X, op, Y, _, Z = expression.split()
        X, Y, Z = int(X), int(Y), int(Z)
        if op == "+":
            result.append("O" if X + Y == Z else "X")
        else:
            result.append("O" if X - Y == Z else "X")
    return result
