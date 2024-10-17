def solution(my_string):
    new_string = []
    for char in my_string:
        if char not in new_string:
            new_string.append(char)
    return "".join(new_string)
