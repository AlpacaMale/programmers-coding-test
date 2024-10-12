def solution(myString):
    return "".join("A" if char in "aA" else char.lower() for char in myString)
