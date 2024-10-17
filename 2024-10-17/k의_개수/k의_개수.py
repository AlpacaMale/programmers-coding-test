def solution(i, j, k):
    k = str(k)
    return "".join(str(number) for number in range(i, j + 1)).count(k)
