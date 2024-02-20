def solution(angle):
    return [[1, 2], [3, 4]][angle > 90][angle % 90 == 0]
