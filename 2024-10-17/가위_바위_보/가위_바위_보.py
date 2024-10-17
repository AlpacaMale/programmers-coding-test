def solution(rsp):
    wins = {"2": "0", "0": "5", "5": "2"}
    result = []
    for hand in rsp:
        result.append(wins[hand])
    return "".join(result)
