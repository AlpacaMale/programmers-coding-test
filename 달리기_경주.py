def solution(players, callings):
    player_index = {player: index for index, player in enumerate(players)}
    for calling in callings:
        index = player_index[calling]
        prev_index = index - 1
        players[index], players[prev_index] = players[prev_index], players[index]
        player_index[players[index]], player_index[players[prev_index]] = (
            index,
            prev_index,
        )
    return players
