def solution(d, budget):
    d.sort()
    for index in range(len(d)):
        if sum(d[: index + 1]) > budget:
            return index
    return len(d)
