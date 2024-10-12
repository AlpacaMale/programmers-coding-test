def solution(myString, pat):
    new_string = "".join("B" if char == "A" else "A" for char in myString)
    return 1 if pat in new_string else 0
