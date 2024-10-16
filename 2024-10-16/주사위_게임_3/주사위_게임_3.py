from collections import Counter


def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = Counter(dice)

    if len(counts) == 1:
        return 1111 * a

    elif len(counts) == 2:
        if 3 in counts.values():
            p = max(counts, key=lambda x: counts[x])
            q = min(counts, key=lambda x: counts[x])
            return (10 * p + q) ** 2
        else:
            p, q = counts.keys()
            return (p + q) * abs(p - q)

    elif len(counts) == 3:
        q, r = [key for key, value in counts.items() if value == 1]
        return q * r

    else:
        return min(dice)
