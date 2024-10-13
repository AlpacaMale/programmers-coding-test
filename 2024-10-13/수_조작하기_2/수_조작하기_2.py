def solution(numLog):
    control = []
    for index, num in enumerate(numLog):
        if index == 0:
            continue
        prev_num = numLog[index - 1]
        if num - prev_num == 1:
            control.append("w")
        elif num - prev_num == -1:
            control.append("s")
        elif num - prev_num == 10:
            control.append("d")
        else:
            control.append("a")
    return "".join(control)
