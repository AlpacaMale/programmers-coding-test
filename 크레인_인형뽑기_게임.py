def solution(board, moves):
    basket = []
    result = 0
    for move in moves:
        for line in board:
            if line[move - 1]:
                if not basket or basket[-1] != line[move - 1]:
                    basket.append(line[move - 1])
                else:
                    basket.pop()
                    result += 2
                line[move - 1] = 0
                break
    return result
