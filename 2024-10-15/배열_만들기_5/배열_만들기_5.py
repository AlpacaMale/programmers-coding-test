def solution(intStrs, k, s, l):
    numbers = []
    for string in intStrs:
        number = int(string[s : s + l])
        if number > k:
            numbers.append(number)
    return numbers
