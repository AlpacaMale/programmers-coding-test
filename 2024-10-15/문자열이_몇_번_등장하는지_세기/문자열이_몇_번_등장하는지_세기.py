def solution(myString, pat):
    count = 0
    for index in range(len(myString)):
        if myString[index:].startswith(pat):
            count += 1
    return count
