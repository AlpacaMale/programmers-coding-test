def solution(s):
    result = []
    for index, char in enumerate(s):
        sub = s[:index][::-1]
        result.append(sub.find(char) + (char in sub))
    return result
