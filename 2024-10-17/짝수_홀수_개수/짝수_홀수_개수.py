def solution(num_list):
    counter = [0, 0]
    for num in num_list:
        if num % 2 == 0:
            counter[0] += 1
        else:
            counter[1] += 1
    return counter
