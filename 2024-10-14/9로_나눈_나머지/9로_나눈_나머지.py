def solution(number):
    return sum(int(char) for char in number) % 9
