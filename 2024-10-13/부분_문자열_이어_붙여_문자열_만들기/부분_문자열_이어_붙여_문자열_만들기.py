def solution(my_string, parts):
    return "".join(string[s : e + 1] for string, [s, e] in zip(my_string, parts))
