def solution(number):
    combination_array = []
    for first in range(len(number)):
        for second in range(first + 1, len(number)):
            for third in range(second + 1, len(number)):
                combination_array.append([number[first], number[second], number[third]])
    return sum(not sum(numbers) for numbers in combination_array)
