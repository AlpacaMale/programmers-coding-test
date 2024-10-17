def solution(my_string):
    numbers = []
    buff = ""
    for char in my_string:
        if char.isdigit():
            buff += char
        elif buff:
            numbers.append(int(buff))
            buff = ""
    if buff:
        numbers.append(int(buff))
    return sum(numbers)
