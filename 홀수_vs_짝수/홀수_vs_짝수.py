def solution(num_list):
    sum_of_value_of_even_index = 0
    sum_of_value_of_odd_index = 0
    for index, num in enumerate(num_list):
        if index % 2 == 0:
            sum_of_value_of_odd_index += num
        else:
            sum_of_value_of_even_index += num
    return max(sum_of_value_of_even_index, sum_of_value_of_odd_index)
