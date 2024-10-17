movement = {
    "up": (0, 1),
    "down": (0, -1),
    "left": (-1, 0),
    "right": (1, 0),
}


def solution(keyinput, board):
    max_width = board[0] // 2
    min_width = -max_width
    max_height = board[1] // 2
    min_height = -max_height
    current = [0, 0]
    for key in keyinput:
        move_x, move_y = movement[key]
        if (
            min_width <= current[0] + move_x <= max_width
            and min_height <= current[1] + move_y <= max_height
        ):
            current[0] += move_x
            current[1] += move_y
    return current
