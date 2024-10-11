def solution(numbers, hand):
    lthumb_pos, rthumb_pos = 10, 12
    numbers = list(map(lambda x: 11 if x == 0 else x, numbers))
    result = ""
    right_key = [3, 6, 9]
    middle_key = [2, 5, 8, 11]
    left_key = [1, 4, 7]
    for num in numbers:
        lmove = abs((lthumb_pos - 1) // 3 - (num - 1) // 3) + abs(
            (lthumb_pos - 1) % 3 - (num - 1) % 3
        )
        rmove = abs((rthumb_pos - 1) // 3 - (num - 1) // 3) + abs(
            (rthumb_pos - 1) % 3 - (num - 1) % 3
        )
        if num in left_key or (
            num in middle_key and (lmove < rmove or (lmove == rmove and hand == "left"))
        ):
            result += "L"
            lthumb_pos = num
        else:
            result += "R"
            rthumb_pos = num

    return result
