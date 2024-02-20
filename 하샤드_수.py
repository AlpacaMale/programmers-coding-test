def solution(x):
    return not x % sum(int(char) for char in str(x))
