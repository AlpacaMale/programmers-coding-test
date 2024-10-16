def solution(my_string):
    frequency_table = [0] * 52
    for char in my_string:
        index = ord(char) - 65 if ord(char) < 91 else ord(char) - 71
        frequency_table[index] += 1
    return frequency_table
