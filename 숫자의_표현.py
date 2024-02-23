def solution(n):
    result = 0
    for i in range(1, n + 1):
        sequence = []
        for j in range(i, n + 1):
            sequence.append(j)
            if sum(sequence) == n:
                result += 1
                break
            elif sum(sequence) > n:
                break
    return result
