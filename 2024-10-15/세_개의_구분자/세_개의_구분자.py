def solution(myStr):
    new_string = myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()
    return new_string or ["EMPTY"]
