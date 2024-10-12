def solution(myString):
    return "".join("l" if "l" > char else char for char in myString)
