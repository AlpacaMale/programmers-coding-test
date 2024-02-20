def solution(rsp):
    #딕셔너리를 이용해서 값 변환
    win_table = {"2": "0", "0": "5", "5": "2"}
    return "".join(win_table[i] for i in rsp)
