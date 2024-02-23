def solution(park, routes):
    dog_pos = find_start(park)
    max_x = len(park) - 1
    max_y = len(park[0]) - 1
    for route in routes:
        index = 1 if route[0] in ["S", "E"] else -1
        move = True
        x_pos = dog_pos[0]
        y_pos = dog_pos[1]
        for _ in range(int(route[2])):
            if (
                move
                and route[0] in ["N", "S"]
                and not (
                    x_pos + index < 0
                    or x_pos + index > max_x
                    or park[x_pos + index][dog_pos[1]] == "X"
                )
            ):
                x_pos += index
            elif (
                move
                and route[0] in ["E", "W"]
                and not (
                    y_pos + index < 0
                    or y_pos + index > max_y
                    or park[dog_pos[0]][y_pos + index] == "X"
                )
            ):
                y_pos += index
            else:
                move = False
        if move and route[0] in ["N", "S"]:
            dog_pos[0] += index * int(route[2])
        elif move and route[0] in ["E", "W"]:
            dog_pos[1] += index * int(route[2])
    return dog_pos


def find_start(park):
    for row in range(len(park)):
        if "S" in park[row]:
            col = park[row].find("S")
            return [row, col]
