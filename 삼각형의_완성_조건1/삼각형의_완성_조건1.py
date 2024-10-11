def solution(sides):
    side_1, side_2, side_3 = sorted(sides)
    return [2, 1][side_1 + side_2 > side_3]
