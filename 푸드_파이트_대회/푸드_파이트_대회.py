def solution(food):
    result = ""
    for index, value in enumerate(food[1:]):
        result += str(index + 1) * (value // 2)
    return result + "0" + result[::-1]
