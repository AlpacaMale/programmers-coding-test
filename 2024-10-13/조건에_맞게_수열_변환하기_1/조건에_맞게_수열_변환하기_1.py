def process_number(num):
    if num >= 50 and num % 2 == 0:
        return num / 2
    elif num < 50 and num % 2 == 1:
        return num * 2
    else:
        return num


def solution(arr):
    return [process_number(num) for num in arr]
