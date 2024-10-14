def solution(str1, str2):
    return "".join(char1 + char2 for char1, char2 in zip(str1, str2))
