def solution(strArr):
    return [
        string.lower() if index % 2 == 0 else string.upper()
        for index, string in enumerate(strArr)
    ]
