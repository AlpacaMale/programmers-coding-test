def solution(num_list):
    x, y = "", ""
    for num in num_list:
        if num % 2:
            x += str(num)
        else:
            y += str(num)
    return int(x) + int(y)
