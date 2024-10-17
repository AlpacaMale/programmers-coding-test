def solution(my_string):
    return "".join(char for char in my_string if char not in "aeiou")
