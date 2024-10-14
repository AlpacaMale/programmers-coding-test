def solution(a, d, included):
    sequence = [a + (d * n) for n in range(len(included))]
    return sum(value for value, is_included in zip(sequence, included) if is_included)
