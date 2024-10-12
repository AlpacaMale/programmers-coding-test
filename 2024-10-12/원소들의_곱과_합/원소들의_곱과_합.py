import math


def solution(num_list):
    total_square = sum(num_list) ** 2
    total_power = math.prod(num_list)
    return 1 if total_square > total_power else 0
