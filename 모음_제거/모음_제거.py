def solution(my_string):
    gather = "aeiou"
    return "".join(char for char in my_string if not char in gather)
