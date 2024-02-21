def solution(keymap, targets):
    result = []
    key_to_index = {}
    for values in keymap:
        for index, value in enumerate(values):
            if value not in key_to_index or key_to_index[value] > index + 1:
                key_to_index[value] = index + 1

    for target in targets:
        target_indices = [key_to_index.get(char, -1) for char in target]
        offset_sum = [-1, sum(target_indices)][-1 not in target_indices]
        result.append(offset_sum)

    return result
