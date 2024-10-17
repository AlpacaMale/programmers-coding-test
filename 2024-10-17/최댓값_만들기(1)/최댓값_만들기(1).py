def solution(numbers):
    max1, max2 = 0, 0
    for number in numbers:
        if number > max1:
            max1, max2 = number, max1
        elif number > max2:
            max2 = number
    return max1 * max2
