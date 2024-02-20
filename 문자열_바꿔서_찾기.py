def solution(myString, pat):
    return (pat in "".join("A" if char == "B" else "B" for char in myString)) / 1
