def solution(k, m, score):
    good_apples = sorted(score, reverse=True)[: len(score) - len(score) % m]
    return sum(
        min(good_apples[box * m : box * m + m]) * m
        for box in range(len(good_apples) // m)
    )
