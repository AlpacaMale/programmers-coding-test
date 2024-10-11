def solution(dartResult):
    dart_scores = [0, 0, 0]
    bonus_info = {"S": 1, "D": 2, "T": 3}
    option_info = {"*": 2, "#": -1}

    buffer = ""
    current_index = 0

    for char in dartResult:
        if char.isdigit():
            buffer += char
        elif char in bonus_info:
            dart_scores[current_index] = int(buffer) ** bonus_info[char]
            buffer = ""
            current_index += 1
        elif char in option_info:
            dart_scores[current_index - 1] *= option_info[char]
            if char == "*":
                dart_scores[current_index - 2] *= option_info[char]

    return sum(dart_scores)
