def solution(my_string):
    numbers = my_string.replace("+ ", "+").replace("- ", "-").split()
    return sum(int(number) for number in numbers)
