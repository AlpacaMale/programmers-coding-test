def solution(t, p):
    paticial_list = [
        t[number : number + len(p)] for number in range(len(t) - len(p) + 1)
    ]
    return sum(number <= p for number in paticial_list)
