def solution(survey, choices):
    personal_types = {char: 0 for char in ["R", "T", "C", "F", "J", "M", "A", "N"]}
    survey_result = ""

    for index, choice in zip(survey, choices):
        if choice in [1, 2, 3]:
            personal_types[index[0]] += 4 - choice
        elif choice in [5, 6, 7]:
            personal_types[index[1]] += choice - 4

    for index in ["RT", "CF", "JM", "AN"]:
        if personal_types[index[0]] >= personal_types[index[1]]:
            survey_result += index[0]
        else:
            survey_result += index[1]

    return survey_result
