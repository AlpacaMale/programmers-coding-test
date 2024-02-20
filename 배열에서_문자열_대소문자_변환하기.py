def solution(strArr):
    return [
        string.upper() if index % 2 else string.lower()
        for index, string in enumerate(strArr)
    ]
