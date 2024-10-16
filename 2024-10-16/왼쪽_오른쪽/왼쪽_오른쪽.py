def solution(str_list):
    for index, char in enumerate(str_list):
        if char == "l":
            return str_list[:index]
        elif char == "r":
            return str_list[index + 1 :]
    return []
