def solution(board):
    len_x = len(board[0])
    len_y = len(board)
    count = 0
    for cur_x in range(len_x):
        for cur_y in range(len_y):
            found = False
            for x in [cur_x - 1, cur_x, cur_x + 1]:
                if 0 <= x < len_x:
                    for y in [cur_y - 1, cur_y, cur_y + 1]:
                        if 0 <= y < len_y and board[y][x] == 1:
                            found = True
                            break
            if found:
                count += 1

    return len_x * len_y - count
