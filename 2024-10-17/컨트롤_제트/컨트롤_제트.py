def solution(s):
    numbers = []
    buff = ""
    for char in s:
        if char.isdigit() or char == "-":
            buff += char
        elif char == "Z":
            numbers.pop()
        elif buff:
            numbers.append(int(buff))
            buff = ""
    if buff:
        numbers.append(int(buff))
    return sum(numbers)
