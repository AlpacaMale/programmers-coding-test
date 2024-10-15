def solution(my_string, indices):
    return "".join(char for index, char in enumerate(my_string) if index not in indices)
