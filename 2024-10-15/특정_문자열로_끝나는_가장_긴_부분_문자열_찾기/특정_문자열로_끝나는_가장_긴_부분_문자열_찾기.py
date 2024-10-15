def solution(myString, pat):
    e = myString.rindex(pat) + len(pat)
    return myString[:e]
