RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)


def solution(n):
    matrix = [[0] * n for _ in range(n)]
    directions = [RIGHT, DOWN, LEFT, UP]
    direction_index = 0
    x, y = 0, 0
    counter = 1

    while counter <= n**2:
        matrix[y][x] = counter
        counter += 1

        next_y = y + directions[direction_index][0]
        next_x = x + directions[direction_index][1]

        if not (0 <= next_y < n and 0 <= next_x < n and matrix[next_y][next_x] == 0):
            direction_index = (direction_index + 1) % 4
            next_y = y + directions[direction_index][0]
            next_x = x + directions[direction_index][1]

        x, y = next_x, next_y

    return matrix
