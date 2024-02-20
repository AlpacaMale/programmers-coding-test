def solution(dot):
    x, y = dot
    return [[1, 4], [2, 3]][x < 0][y < 0]
