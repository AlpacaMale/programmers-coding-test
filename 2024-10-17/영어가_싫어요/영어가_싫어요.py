string_to_number = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(numbers):
    for string, number in string_to_number.items():
        numbers = numbers.replace(string, number)
    return int(numbers)
