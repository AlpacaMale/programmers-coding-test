def solution(s):
    result = ""
    for index, char in enumerate(s):
        result += (
            char.lower() if (index - s[:index].rfind(" ") + 1) % 2 else char.upper()
        )
    return result
