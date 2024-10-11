def solution(answers):
    pattern0 = [1, 2, 3, 4, 5]
    pattern1 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    length0, length1, length2 = len(pattern0), len(pattern1), len(pattern2)
    result = [0, 0, 0]
    for index, right_answer in enumerate(answers):
        result[0] += (pattern0[index % length0] == right_answer) / 1
        result[1] += (pattern1[index % length1] == right_answer) / 1
        result[2] += (pattern2[index % length2] == right_answer) / 1
    highest_point = max(result)
    return [index + 1 for index, point in enumerate(result) if highest_point == point]
