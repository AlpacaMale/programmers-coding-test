def solution(array, height):
    return sum(1 for _height in array if _height > height)
