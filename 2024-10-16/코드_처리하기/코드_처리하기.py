def solution(codes):
    ret = []
    mode = False
    for index, code in enumerate(codes):
        if code == "1":
            mode = not mode
        elif index % 2 == int(mode):
            ret.append(code)
    return "".join(ret) or "EMPTY"
