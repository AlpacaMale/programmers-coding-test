def solution(my_string):
    return "".join(
        char.upper() if char.islower() else char.lower() for char in my_string
    )
