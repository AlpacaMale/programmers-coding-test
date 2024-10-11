def solution(num_list):
    total_square = sum(num_list) ** 2
    total_power = 1
    for num in num_list:
        total_power *= num
    return 1 if total_square > total_power else 0
